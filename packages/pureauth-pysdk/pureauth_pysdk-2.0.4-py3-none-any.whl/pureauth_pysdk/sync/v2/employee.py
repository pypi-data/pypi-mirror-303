import base64
import os
from hashlib import pbkdf2_hmac, sha256
from typing import List

import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from pureauth_pysdk.dto import PureAUTHServerConfigDTO
from pureauth_pysdk.utils import batch_list, employee_id, sign_dataset, verify_dataset

from ..errors import (
    ActivateEmployeeApiError,
    DatasetFormatError,
    DeactivateEmployeeApiError,
    GroupAttachApiError,
    JSONDecodeError,
    PureAUTHApiError,
    RoleAttachApiError,
    SignatureApiError,
    StatusApiError,
    UserAddApiError,
    UserUpdateApiError,
    WelcomeEmailApiError,
    AutoOSMFetchApiError,
)
from .dto import (
    ApiUri,
    EmployeeAccessMappingDTO,
    EmployeeDatasetDTO,
    EmployeePrimaryDatasetDTO,
)
from .organization import Organization


class Employee:
    def __init__(self, config: PureAUTHServerConfigDTO, organization: Organization):
        """Initialize Emploee class with parameters to call PureAUTH API.

        Args:
            config (PureAUTHServerConfigDTO): PureAUTH config object. (private key is required)
            organization (Organization): Organization object to get datasets
        """
        self.config = config
        self.url = ApiUri(config=config)
        self.request_headers = {
            "Organization-Id": self.config.organization_id,
            "Access-Token": self.config.access_token,
        }
        self.organization = organization

    def status(self, corporate_emails: List[str], batch_size=500) -> list:
        """Get Employee status from PureAUTH

        Args:
            corporate_email (List[str]): Employee corporate emails list.
            batch_size: Number of objects per request

        Raises:
            StatusApiError
            PureAUTHApiError
            JSONDecodeError

        Returns:
            dict: Object containing employee status.
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for corporate_emails_batch in batch_list(
            corporate_emails, batch_size=batch_size
        ):
            results += self._status(corporate_emails=corporate_emails_batch)
        return results

    def _status(self, corporate_emails: List[str]) -> list:
        try:
            identifiers: list = []
            identifiers_map: dict = {}
            for _corporate_email in corporate_emails:
                corporate_email = _corporate_email.strip().lower()
                emp_id = employee_id(self.config.organization_id, corporate_email)
                identifiers.append(emp_id)
                identifiers_map[emp_id] = corporate_email
            res = requests.post(
                self.url.employee_status_url(),
                headers=self.request_headers,
                json={"identifiers": identifiers},
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise StatusApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results

        except Exception as e:
            raise PureAUTHApiError(e)

    def add(
        self,
        employee_datasets: List[EmployeeDatasetDTO],
        send_email: bool = False,
        batch_size=250,
    ) -> list:
        """Add new employee to the PureAUTH platform

        Args:
            employee_datasets (List[EmployeeDatasetDTO]): Employee data containing Primary and Secondary datasets.
            send_email (bool, optional): Send welcome email. Defaults to False.
            batch_size (int): Number of objects per request

        Raises:
            UserAddApiError
            PureAUTHApiError

        Returns:
            bool: List[dict]
        """
        # Limit batch size to 250
        batch_size = min(batch_size, 250)
        results = []
        for employee_datasets_batch in batch_list(
            employee_datasets, batch_size=batch_size
        ):
            results += self._add(
                employee_datasets=employee_datasets_batch, send_email=send_email
            )
        return results

    def _add(
        self, employee_datasets: List[EmployeeDatasetDTO], send_email: bool = False
    ) -> bool:

        try:
            datasets = self.organization.datasets()
            request_body: List[dict] = []
            identifiers_map_ds: dict = {}
            for employee_dataset in employee_datasets:
                if employee_dataset.primary_dataset.corporate_email == "":
                    continue
                identifier = employee_id(
                    self.config.organization_id,
                    employee_dataset.primary_dataset.corporate_email,
                )
                identifiers_map_ds[identifier] = employee_dataset.primary_dataset
                employee_signature_list = []
                for dataset in datasets:
                    if dataset.get("encrypted"):
                        encrypted_extra_attributes = self._aes_encrypt(
                            employee_dataset.secondary_dataset.serialized,
                            self._generate_aes_key(
                                employee_data=employee_dataset.primary_dataset
                            ),
                        )
                        if encrypted_extra_attributes is None:
                            continue
                        extra_attributes_for_signature = (
                            employee_dataset.secondary_dataset.serialized.lower()
                            + employee_dataset.primary_dataset.full_name
                            + employee_dataset.primary_dataset.corporate_email
                            + employee_dataset.primary_dataset.phone_number
                        )
                        employee_signature_list.append(
                            {
                                "dataset_id": dataset.get("public_id"),
                                "signed_data": sign_dataset(
                                    self.config.private_key, encrypted_extra_attributes
                                ),
                                "enc_attributes": encrypted_extra_attributes,
                                "json_signature": sign_dataset(
                                    self.config.private_key,
                                    extra_attributes_for_signature,
                                ),
                            }
                        )
                    else:
                        formatted_primary_ds = self._format_non_encrypted_dataset(
                            dataset=dataset,
                            employee_data=employee_dataset.primary_dataset,
                        )
                        employee_signature_list.append(
                            {
                                "dataset_id": dataset.get("public_id"),
                                "signed_data": sign_dataset(
                                    self.config.private_key, formatted_primary_ds
                                ),
                            }
                        )
                request_object = {
                    "employee_id": identifier,
                    "signatures": employee_signature_list,
                }
                request_body.append(request_object)

            res = requests.post(
                self.url.employee_add_url(),
                json=request_body,
                headers=self.request_headers,
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 201:
                raise UserAddApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            email_list: List[EmployeePrimaryDatasetDTO] = []
            for result in data:
                emp_ds: EmployeePrimaryDatasetDTO = identifiers_map_ds.get(
                    result.get("employee_id")
                )
                if emp_ds:
                    result["corporate_email"] = emp_ds.corporate_email
                    if result.get("status") == "success":
                        email_list.append(emp_ds)
                results.append(result)
            if send_email:
                self.send_welcome_email(email_list)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def update(
        self,
        employee_datasets: List[EmployeeDatasetDTO],
        send_email: bool = False,
        batch_size: int = 500,
    ) -> bool:
        """Update an existing employee on the PureAUTH platform

        Args:
            employee_dataset (List[EmployeeDatasetDTO]): Employee data containing Primary and Secondary datasets.
            send_email (bool, optional): Send welcome email. Defaults to False.
            batch_size (int): Number of objects per request

        Raises:
            UserUpdateApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 250
        batch_size = min(batch_size, 250)
        results = []
        for employee_datasets_batch in batch_list(
            employee_datasets, batch_size=batch_size
        ):
            results += self._update(
                employee_datasets=employee_datasets_batch, send_email=send_email
            )
        return results

    def _update(
        self,
        employee_datasets: List[EmployeeDatasetDTO],
        send_email: bool = False,
    ) -> bool:
        try:
            corporate_email_list = [
                x.primary_dataset.corporate_email for x in employee_datasets
            ]
            datasets = self.organization.datasets()
            signatures = self.signatures(corporate_emails=corporate_email_list)
            signature_id_map = {}
            for sig in signatures:
                if sig.get("status") != "success":
                    continue
                signature_id_map[sig.get("employee_id")] = sig.get("signatures", [])

            request_body: List[dict] = []
            identifiers_map_ds: dict = {}
            for employee_dataset in employee_datasets:
                if employee_dataset.primary_dataset.corporate_email == "":
                    continue
                identifier = employee_id(
                    self.config.organization_id,
                    employee_dataset.primary_dataset.corporate_email,
                )
                identifiers_map_ds[identifier] = {
                    "primary": employee_dataset.primary_dataset,
                    "primary_updated": False,
                }
                employee_signature_list = []
                for dataset in datasets:
                    for signature in signature_id_map[identifier]:
                        if not dataset.get("public_id") == signature.get("public_id"):
                            continue
                        if dataset.get("encrypted"):
                            encrypted_extra_attributes = self._aes_encrypt(
                                employee_dataset.secondary_dataset.serialized,
                                self._generate_aes_key(
                                    employee_data=employee_dataset.primary_dataset
                                ),
                            )
                            if encrypted_extra_attributes is None:
                                continue
                            extra_attributes_for_signature = (
                                employee_dataset.secondary_dataset.serialized.lower()
                                + employee_dataset.primary_dataset.full_name
                                + employee_dataset.primary_dataset.corporate_email
                                + employee_dataset.primary_dataset.phone_number
                            )
                            if not verify_dataset(
                                private_key=self.config.private_key,
                                dataset=extra_attributes_for_signature,
                                signature=signature.get("signature"),
                            ):
                                employee_signature_list.append(
                                    {
                                        "dataset_id": dataset.get("public_id"),
                                        "signed_data": sign_dataset(
                                            self.config.private_key,
                                            encrypted_extra_attributes,
                                        ),
                                        "enc_attributes": encrypted_extra_attributes,
                                        "json_signature": sign_dataset(
                                            self.config.private_key,
                                            extra_attributes_for_signature,
                                        ),
                                    }
                                )
                        else:
                            formatted_primary_ds = self._format_non_encrypted_dataset(
                                dataset=dataset,
                                employee_data=employee_dataset.primary_dataset,
                            )
                            if not verify_dataset(
                                private_key=self.config.private_key,
                                dataset=formatted_primary_ds,
                                signature=signature.get("signature"),
                            ):
                                identifiers_map_ds[identifier]["primary_updated"] = True
                                employee_signature_list.append(
                                    {
                                        "dataset_id": dataset.get("public_id"),
                                        "signed_data": sign_dataset(
                                            self.config.private_key,
                                            formatted_primary_ds,
                                        ),
                                    }
                                )
                if len(employee_signature_list) < 1:
                    continue  # No updated data.
                employee_update_request_body = {
                    "employee_id": identifier,
                    "signatures": employee_signature_list,
                }
                request_body.append(employee_update_request_body)
            res = requests.put(
                self.url.employee_update_url(),
                json=request_body,
                headers=self.request_headers,
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise UserUpdateApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            email_list: List[EmployeePrimaryDatasetDTO] = []
            for result in data:
                emp_result: dict = identifiers_map_ds.get(result.get("employee_id"), {})
                emp_ds: EmployeePrimaryDatasetDTO = emp_result.get("primary")
                if emp_ds and emp_result.get("primary_updated"):
                    result["corporate_email"] = emp_ds.corporate_email
                    if result.get("status") == "success":
                        email_list.append(emp_ds)
                results.append(result)
            if send_email:
                self.send_welcome_email(email_list)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def send_welcome_email(
        self,
        employee_primary_ds_list: List[EmployeePrimaryDatasetDTO],
        batch_size=500,
    ) -> list:
        """Send a welcome email to a user.

        Args:
            employee_primary_ds (List[EmployeePrimaryDatasetDTO]): Employee Primary dataset list.
            batch_size (int): Number of objects per request

        Raises:
            WelcomeEmailApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 250
        batch_size = min(batch_size, 250)
        results = []
        for employee_primary_ds_batch in batch_list(
            employee_primary_ds_list, batch_size=batch_size
        ):
            results += self._send_welcome_email(
                employee_primary_ds_list=employee_primary_ds_batch
            )
        return results

    def _send_welcome_email(
        self, employee_primary_ds_list: List[EmployeePrimaryDatasetDTO]
    ) -> list:
        """Send a welcome email to a user.
        Note: If primary data is missing, the user will be skipped.

        Args:
            employee_primary_ds (List[EmployeePrimaryDatasetDTO]): Employee Primary dataset list.

        Raises:
            WelcomeEmailApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        try:
            request_body: List[dict] = []
            identifiers_map: dict = {}
            for employee_primary_ds in employee_primary_ds_list:
                if employee_primary_ds.corporate_email == "":
                    continue
                if employee_primary_ds.corporate_email == "":
                    continue
                if employee_primary_ds.phone_number == "":
                    continue
                identifier = employee_id(
                    self.config.organization_id, employee_primary_ds.corporate_email
                )
                identifiers_map[identifier] = employee_primary_ds.corporate_email
                request_body.append(employee_primary_ds.user_dataset)
            res = requests.post(
                url=self.url.welcome_email_url(),
                json=request_body,
                headers=self.request_headers,
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise WelcomeEmailApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def activate(self, corporate_emails: List[str], batch_size=500) -> list:
        """Activate an inactive employee.

        Args:
            corporate_email (str): Employee corporate email.
            batch_size (int): Number of objects per request.

        Raises:
            ActivateEmployeeApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for corporate_emails_batch in batch_list(
            corporate_emails, batch_size=batch_size
        ):
            results += self._activate(corporate_emails=corporate_emails_batch)
        return results

    def _activate(self, corporate_emails: List[str]) -> List[dict]:
        try:
            identifiers: list = []
            identifiers_map: dict = {}
            for _corporate_email in corporate_emails:
                corporate_email = _corporate_email.strip().lower()
                emp_id = employee_id(self.config.organization_id, corporate_email)
                identifiers.append(emp_id)
                identifiers_map[emp_id] = corporate_email
            res = requests.put(
                self.url.employee_activate_url(),
                headers=self.request_headers,
                json={"identifiers": identifiers},
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise ActivateEmployeeApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results

        except Exception as e:
            raise PureAUTHApiError(e)

    def deactivate(self, corporate_emails: List[str], batch_size=500) -> list:
        """Deactivate an active employee.

        Args:
            corporate_email (str): Employee corporate email.
            batch_size (int): Number of objects per request.

        Raises:
            DeactivateEmployeeApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for corporate_emails_batch in batch_list(
            corporate_emails, batch_size=batch_size
        ):
            results += self._deactivate(corporate_emails=corporate_emails_batch)
        return results

    def _deactivate(self, corporate_emails: List[str]) -> List[dict]:
        try:
            identifiers: list = []
            identifiers_map: dict = {}
            for _corporate_email in corporate_emails:
                corporate_email = _corporate_email.strip().lower()
                emp_id = employee_id(self.config.organization_id, corporate_email)
                identifiers.append(emp_id)
                identifiers_map[emp_id] = corporate_email
            res = requests.put(
                self.url.employee_deactivate_url(),
                headers=self.request_headers,
                json={"identifiers": identifiers},
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise DeactivateEmployeeApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results

        except Exception as e:
            raise PureAUTHApiError(e)

    # Complete
    def signatures(self, corporate_emails: List[str], batch_size=250) -> list:
        """Get employee dataset signatures.

        Args:
            corporate_email (List[str]): Employee corporate emails list.
            batch_size (int): Number of objects per request.

        Raises:
            SignatureApiError
            PureAUTHApiError
            JSONDecodeError

        Returns:
            list: List of employees and their signatures.
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for corporate_emails_batch in batch_list(
            corporate_emails, batch_size=batch_size
        ):
            results += self._signatures(corporate_emails=corporate_emails_batch)
        return results

    def _signatures(self, corporate_emails: List[str]) -> list:
        try:
            identifiers: list = []
            identifiers_map: dict = {}
            for _corporate_email in corporate_emails:
                corporate_email = _corporate_email.strip().lower()
                emp_id = employee_id(self.config.organization_id, corporate_email)
                identifiers.append(emp_id)
                identifiers_map[emp_id] = corporate_email
            res = requests.post(
                url=self.url.employee_signature_url(),
                headers=self.request_headers,
                json={"identifiers": identifiers},
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise SignatureApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def attach_groups(
        self, employee_datasets: List[EmployeeDatasetDTO], batch_size=250
    ) -> List[dict]:
        """Assign groups to employee

        Args:
            employee_datasets (List[EmployeeDatasetDTO]): List of groups to assign to employees
            using the mapping_dataset field.
            EmployeeDatasetDTO : from pureauth_pysdk.sync.v2.dto import EmployeeDatasetDTO
            batch_size (int): Number of objects per request.
        Raises:
            GroupAttachApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for access_mapping_batch in batch_list(
            employee_datasets, batch_size=batch_size
        ):
            results += self._attach_groups(employee_datasets=access_mapping_batch)
        return results

    def _attach_groups(self, employee_datasets: List[EmployeeDatasetDTO]) -> List[dict]:
        try:
            organization_groups = self.organization.groups()

            request_body: list = []
            identifiers_map: dict = {}
            for dataset in employee_datasets:
                mapping: EmployeeAccessMappingDTO = dataset.mapping_dataset
                emp_id = employee_id(
                    self.config.organization_id, mapping.corporate_email
                )
                identifiers_map[emp_id] = mapping.corporate_email

                group_public_ids = []
                for grp in organization_groups:
                    if grp.get("name") in mapping.groups:
                        group_public_ids.append(grp.get("public_id"))
                request_object = {"groups": group_public_ids, "employee_id": emp_id}
                request_body.append(request_object)

            res = requests.post(
                self.url.employee_group_attach_url(),
                headers=self.request_headers,
                json=request_body,
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise GroupAttachApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def attach_roles(
        self, employee_datasets: List[EmployeeDatasetDTO], batch_size=250
    ) -> List[dict]:
        """Assign roles to employee

        Args:
            employee_datasets (List[EmployeeAccessMappingDTO]): List of roles to assign to employees
            using the mapping_dataset field.
            EmployeeDatasetDTO : from pureauth_pysdk.sync.v2.dto import EmployeeDatasetDTO
            batch_size (int): Number of objects per request.
        Raises:
            RoleAttachApiError
            PureAUTHApiError

        Returns:
            List[dict]
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for access_mapping_batch in batch_list(
            employee_datasets, batch_size=batch_size
        ):
            results += self._attach_roles(employee_datasets=access_mapping_batch)
        return results

    def _attach_roles(self, employee_datasets: List[EmployeeDatasetDTO]) -> List[dict]:
        try:
            organization_roles = self.organization.roles()

            request_body: list = []
            identifiers_map: dict = {}
            for employee_dataset in employee_datasets:
                mapping: EmployeeAccessMappingDTO = employee_dataset.mapping_dataset
                emp_id = employee_id(
                    self.config.organization_id, mapping.corporate_email
                )
                identifiers_map[emp_id] = mapping.corporate_email

                role_public_ids = []
                for role in organization_roles:
                    if role.get("name") in mapping.roles:
                        role_public_ids.append(role.get("public_id"))
                request_object = {"roles": role_public_ids, "employee_id": emp_id}
                request_body.append(request_object)

            res = requests.post(
                self.url.employee_role_attach_url(),
                headers=self.request_headers,
                json=request_body,
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise RoleAttachApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def get_autoosm_codes(self, corporate_emails: List[str], batch_size=250) -> list:
        """Get employee auto_osm codes.

        Args:
            corporate_email (List[str]): Employee corporate emails list.
            batch_size (int): Number of objects per request.

        Raises:
            AutoOSMFetchApiError
            PureAUTHApiError
            JSONDecodeError

        Returns:
            list: List of employees and their auto osm tokens.
        """
        # Limit batch size to 500
        batch_size = min(batch_size, 500)
        results = []
        for corporate_emails_batch in batch_list(
            corporate_emails, batch_size=batch_size
        ):
            results += self._get_autoosm_codes(corporate_emails=corporate_emails_batch)
        return results

    def _get_autoosm_codes(self, corporate_emails: List[str]) -> List[dict]:
        try:
            identifiers: list = []
            identifiers_map: dict = {}
            for _corporate_email in corporate_emails:
                corporate_email = _corporate_email.strip().lower()
                emp_id = employee_id(self.config.organization_id, corporate_email)
                identifiers.append(emp_id)
                identifiers_map[emp_id] = corporate_email
            res = requests.post(
                url=self.url.employee_autoosm_fetch_url(),
                headers=self.request_headers,
                json={
                    "identifiers": identifiers,
                    "data": "hello",
                    "signature": sign_dataset(self.config.private_key, "hello"),
                },
            )
            try:
                data: dict = res.json()
            except Exception as e:
                raise JSONDecodeError(e)
            if res.status_code != 200:
                raise AutoOSMFetchApiError(
                    f"\nstatus_code: {data.get('status_code')}\n"
                    f"error: {data.get('error')}\n"
                    f"message: {data.get('message')}\n"
                    f"attributes: {data.get('attributes')}\n"
                )
            results: list = []
            for result in data:
                corporate_email = identifiers_map.get(result.get("employee_id"))
                if corporate_email:
                    result["corporate_email"] = corporate_email
                results.append(result)
            return results
        except Exception as e:
            raise PureAUTHApiError(e)

    def _format_non_encrypted_dataset(
        self, dataset: dict, employee_data: EmployeePrimaryDatasetDTO
    ):
        try:
            formatted_data = [None] * len(dataset["attributes"])
            for attribute in dataset.get("attributes"):
                formatted_data[attribute["order"] - 1] = employee_data.user_dataset[
                    attribute["name"]
                ]
            return ";".join(formatted_data)
        except Exception as e:
            raise DatasetFormatError(e)

    @staticmethod
    def _generate_aes_key(employee_data: EmployeePrimaryDatasetDTO):
        SALT = "7OwmOZ5WpI8mfSvjGKEbkZRV2KE=".encode()
        ITERATIONS = 1000
        HASHSIZE = 16

        initial_key_factors = (
            employee_data.corporate_email
            + employee_data.phone_number
            + employee_data.full_name
        )
        key_sha_bytes = sha256(initial_key_factors.encode())
        key_hmac = pbkdf2_hmac(
            "sha256",
            key_sha_bytes.hexdigest().upper().encode(),
            SALT,
            ITERATIONS,
            HASHSIZE,
        )
        hmac = base64.b64encode(key_hmac).decode()
        return hmac

    @staticmethod
    def _aes_decrypt(ciphertext: str, key: str) -> str:
        aeskey = sha256(key.encode())
        ciphertext_bytes = base64.b64decode(ciphertext)
        iv = ciphertext_bytes[:16]
        enc_attributes = ciphertext_bytes[16:]
        cipher = Cipher(
            algorithms.AES(aeskey.digest()), modes.CTR(iv), backend=default_backend()
        )
        decryptor = cipher.decryptor()
        dt = decryptor.update(enc_attributes)

        return dt.decode("utf-8")

    @staticmethod
    def _aes_encrypt(data: str, key: str) -> str:
        try:
            aeskey = sha256(key.encode())
            data_bytes = data.encode()
            iv = os.urandom(16)
            cipher = Cipher(
                algorithms.AES(aeskey.digest()),
                modes.CTR(iv),
                backend=default_backend(),
            )
            encryptor = cipher.encryptor()
            ct = encryptor.update(data_bytes) + encryptor.finalize()
            final_ciphertext = iv + ct
            return base64.b64encode(final_ciphertext).decode()
        except Exception as _:
            return None
