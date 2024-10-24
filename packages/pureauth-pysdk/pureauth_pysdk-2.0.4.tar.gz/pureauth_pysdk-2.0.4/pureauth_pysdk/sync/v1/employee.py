import base64
import os
from hashlib import pbkdf2_hmac, sha256
from typing import List

import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from pureauth_pysdk.dto import PureAUTHServerConfigDTO
from pureauth_pysdk.utils import employee_id, sign_dataset, verify_dataset

from ..errors import (
    ActivateEmployeeApiError,
    DatasetFormatError,
    GroupAttachApiError,
    PureAUTHApiError,
    RoleAttachApiError,
    StatusApiError,
    UserAddApiError,
    UserUpdateApiError,
    WelcomeEmailApiError,
)
from .dto import (
    ApiUri,
    EmployeeDatasetDTO,
    EmployeePrimaryDatasetDTO,
    EmployeeStatusDTO,
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

    def status(self, corporate_email: str) -> EmployeeStatusDTO:
        """Get Employee status from PureAUTH

        Args:
            corporate_email (str): Employee corporate email.

        Raises:
            StatusApiError
            PureAUTHApiError

        Returns:
            pureauth_pysdk.sync.dto.EmployeeStatusDTO: Object containing employee status.
        """
        try:
            emp_id = employee_id(self.config.organization_id, corporate_email)
            res = requests.post(
                self.url.employee_status_url(emp_id), headers=self.request_headers
            )
            data = res.json()
            if data["status"] == "failure":
                error_code = data.get("code")
                if error_code == 1009:
                    return EmployeeStatusDTO(
                        is_active=False, osm="unverified", onboarded=False
                    )
                error = data.get("user_error")
                raise StatusApiError(f"{res.status_code}: {error}")
            if data["status"] == "success":
                return EmployeeStatusDTO(
                    is_active=data["data"]["is_active"],
                    osm=data["data"]["osm"],
                    onboarded=True,
                )
        except Exception as e:
            raise PureAUTHApiError(e)

    def add(
        self, employee_dataset: EmployeeDatasetDTO, send_email: bool = False
    ) -> bool:
        """Add new employee to the PureAUTH platform

        Args:
            employee_dataset (EmployeeDatasetDTO): Employee data containing Primary and Secondary datasets.
            send_email (bool, optional): Send welcome email. Defaults to False.

        Raises:
            UserAddApiError
            PureAUTHApiError

        Returns:
            bool: Success
        """
        try:
            datasets = self.organization.datasets()
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
                                self.config.private_key, extra_attributes_for_signature
                            ),
                        }
                    )
                else:
                    formatted_primary_ds = self._format_non_encrypted_dataset(
                        dataset=dataset, employee_data=employee_dataset.primary_dataset
                    )
                    employee_signature_list.append(
                        {
                            "dataset_id": dataset.get("public_id"),
                            "signed_data": sign_dataset(
                                self.config.private_key, formatted_primary_ds
                            ),
                        }
                    )
            employee_add_request_body = {
                "emp_id": employee_id(
                    self.config.organization_id,
                    employee_dataset.primary_dataset.corporate_email,
                ),
                "signatures": employee_signature_list,
            }

            upload_res = requests.post(
                self.url.employee_add_url(),
                json=employee_add_request_body,
                headers=self.request_headers,
            )
            data = upload_res.json()
            if data["status"] == "success":
                if send_email:
                    self.send_welcome_email(employee_dataset.primary_dataset)
                return True
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise UserAddApiError(error)
        except Exception as e:
            raise PureAUTHApiError(e)

    def update(
        self,
        employee_dataset: EmployeeDatasetDTO,
        send_email: bool = False,
    ) -> bool:
        """Update an existing employee on the PureAUTH platform

        Args:
            employee_dataset (EmployeeDatasetDTO): Employee data containing Primary and Secondary datasets.
            send_email (bool, optional): Send welcome email. Defaults to False.

        Raises:
            UserUpdateApiError
            PureAUTHApiError

        Returns:
            bool: Updated / Already Up-to-date
        """
        try:
            datasets = self.organization.datasets()
            signatures = self.signatures(
                corporate_email=employee_dataset.primary_dataset.corporate_email
            )

            flag_primary_ds_updated = False

            emp_id = employee_id(
                self.config.organization_id,
                employee_dataset.primary_dataset.corporate_email,
            )
            employee_signature_list = []
            for dataset in datasets:
                for signature in signatures:
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
                            flag_primary_ds_updated = True
                            employee_signature_list.append(
                                {
                                    "dataset_id": dataset.get("public_id"),
                                    "signed_data": sign_dataset(
                                        self.config.private_key, formatted_primary_ds
                                    ),
                                }
                            )
            if len(employee_signature_list) < 1:
                return False  # No updated data.
            employee_update_request_body = {
                "signatures": employee_signature_list,
            }
            upload_res = requests.patch(
                self.url.employee_update_url(employee_id=emp_id),
                json=employee_update_request_body,
                headers=self.request_headers,
            )
            data = upload_res.json()
            if data["status"] == "success":
                if send_email and flag_primary_ds_updated:
                    self.send_welcome_email(employee_dataset.primary_dataset)
                return True
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise UserUpdateApiError(error)
        except Exception as e:
            raise PureAUTHApiError(e)

    def send_welcome_email(
        self, employee_primary_ds: EmployeePrimaryDatasetDTO
    ) -> bool:
        """Send a welcome email to a user.

        Args:
            employee_primary_ds (EmployeePrimaryDatasetDTO): Employee Primary dataset.

        Raises:
            WelcomeEmailApiError
            PureAUTHApiError

        Returns:
            bool: Success / Failure
        """
        try:
            emp_id = employee_id(
                self.config.organization_id, employee_primary_ds.corporate_email
            )
            emp_email_req = {
                "organization_id": self.config.organization_id,
                "primary_dataset": employee_primary_ds.user_dataset,
            }
            res = requests.post(
                url=self.url.welcome_email_url(employee_id=emp_id),
                json=emp_email_req,
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                return True
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise WelcomeEmailApiError(error)

        except Exception as e:
            raise PureAUTHApiError(e)

    def activate(self, corporate_email: str) -> bool:
        """Activate an inactive employee.

        Args:
            corporate_email (str): Employee corporate email.

        Raises:
            ActivateEmployeeApiError
            PureAUTHApiError

        Returns:
            bool
        """
        try:
            emp_id = employee_id(self.config.organization_id, corporate_email)
            res = requests.post(
                url=self.url.employee_activate_url(employee_id=emp_id),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                return True
            elif data["status"] == "failure":
                if data.get("code") == 1030:
                    return True
                error = data.get("user_error")
                raise ActivateEmployeeApiError(error)

        except Exception as e:
            raise PureAUTHApiError(e)

    def deactivate(self, corporate_email: str) -> bool:
        """Deactivate an employee

        Args:
            corporate_email (str): Employee corporate email.

        Raises:
            ActivateEmployeeApiError
            PureAUTHApiError

        Returns:
            bool
        """
        try:
            emp_id = employee_id(self.config.organization_id, corporate_email)
            res = requests.post(
                url=self.url.employee_deactivate_url(employee_id=emp_id),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                return True
            elif data["status"] == "failure":
                if data.get("code") == 1022:
                    return True
                error = data.get("user_error")
                raise ActivateEmployeeApiError(error)

        except Exception as e:
            raise PureAUTHApiError(e)

    def signatures(self, corporate_email: str) -> List[str]:
        """Get employee dataset signatures.

        Args:
            corporate_email (str): Employee corporate email.

        Raises:
            ActivateEmployeeApiError
            PureAUTHApiError

        Returns:
            List[str]: List of signatures for each dataset. e.g.
            [
                {
                'public_id': '93258db8-6fe0-48ce-b3c5-xxxxxxxxxxxx',
                'signature': 'MEUCIFZ/<sig>+Zcoxa64GZzT4U+plwRGDbSjw='
                }
            ]
        """
        try:
            emp_id = employee_id(self.config.organization_id, corporate_email)
            res = requests.get(
                url=self.url.employee_signature_url(employee_id=emp_id),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                return data["data"]["signatures"]
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise ActivateEmployeeApiError(error)

        except Exception as e:
            raise PureAUTHApiError(e)

    def attach_groups(self, corporate_email: str, groups: List[str]) -> bool:
        """Assign groups to employee

        Args:
            corporate_email (str): Employee corporate email.
            groups (List[str]): List of groups to assign.

        Raises:
            GroupAttachApiError
            PureAUTHApiError

        Returns:
            bool
        """
        try:
            emp_id = employee_id(
                self.config.organization_id,
                corporate_email,
            )
            organization_groups = self.organization.groups()
            group_public_ids = []
            for grp in organization_groups:
                if grp.get("name") in groups:
                    group_public_ids.append(grp.get("public_id"))
            if not group_public_ids:
                return False
            request_data = {"groups": group_public_ids}
            res = requests.post(
                self.url.employee_group_attach_url(employee_id=emp_id),
                headers=self.request_headers,
                json=request_data,
            )
            data = res.json()
            if data["status"] == "success":
                return True
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise GroupAttachApiError(error)
        except Exception as e:
            raise PureAUTHApiError(e)

    def attach_roles(self, corporate_email: str, roles: List[str]) -> bool:
        """Assign roles to employees

        Args:
            corporate_email (str): Employee corporate email.
            roles (List[str]): List of roles to assign.

        Raises:
            RoleAttachApiError
            PureAUTHApiError

        Returns:
            bool
        """
        try:
            emp_id = employee_id(
                self.config.organization_id,
                corporate_email,
            )
            organization_roles = self.organization.roles()
            role_public_ids = []
            for role in organization_roles:
                if role.get("name") in roles:
                    role_public_ids.append(role.get("public_id"))
            if not role_public_ids:
                return False
            request_data = {"roles": role_public_ids}
            res = requests.post(
                self.url.employee_role_attach_url(employee_id=emp_id),
                headers=self.request_headers,
                json=request_data,
            )
            data = res.json()
            if data["status"] == "success":
                return True
            elif data["status"] == "failure":
                error = data.get("user_error")
                raise RoleAttachApiError(error)
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
