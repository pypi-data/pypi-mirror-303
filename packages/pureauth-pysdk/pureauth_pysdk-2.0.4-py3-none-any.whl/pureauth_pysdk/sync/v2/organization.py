from datetime import datetime
from typing import Dict, List

import requests

from pureauth_pysdk.dto import PureAUTHServerConfigDTO
from pureauth_pysdk.utils import employee_id, sign_dataset

from ..errors import (
    DatasetCsvApiError,
    DatasetListApiError,
    OrganizationGroupsApiError,
    OrganizationLogsApiError,
    OrganizationLogsDateFormatError,
    PublicKeyUploadApiError,
    PureAUTHApiError,
)
from .dto import ApiUri, LogsDTO


class Organization:
    def __init__(self, config: PureAUTHServerConfigDTO):
        """Initialize organization class with parameters to call PureAUTH API.

        Args:
            config (PureAUTHServerConfigDTO): PureAUTH config object. (private key is optional)
        """
        self.config = config
        self.url = ApiUri(config=config)
        self.request_headers = {
            "Organization-Id": self.config.organization_id,
            "Access-Token": self.config.access_token,
        }

    def upload_publickey(self, publickey: str) -> bool:
        """Upload organization Public key

        Args:
            publickey (str): Public key string with begin and end tags

        Raises:
            PureAUTHApiError: API error

        Returns:
            bool: Success / Failure
        """
        try:
            res = requests.post(
                self.url.public_key_upload_url(),
                headers=self.request_headers,
                json={
                    "public_key": publickey,
                    "data": "hello",
                    "signature": sign_dataset(self.config.private_key, "hello"),
                },
            )
            data = res.json()
            if data["status"] == "failure":
                error = data.get("user_error")
                raise PublicKeyUploadApiError(f"{res.status_code}: {error}")
            if data["status"] == "success":
                return True
        except Exception as e:
            raise PureAUTHApiError(e)

    def fetch_csv_template(self) -> str:
        """Fetch dataset CSV template

        Raises:
            PureAUTHApiError: API error

        Returns:
            str: CSV template in string format.
        """
        try:
            res = requests.get(self.url.fetch_csv_url(), headers=self.request_headers)
            if res.status_code != 200:
                error = res.json().get("user_error")
                raise DatasetCsvApiError(f"{res.status_code}: {error}")
            return res.content.decode("utf-8")
        except Exception as e:
            raise PureAUTHApiError(e)

    def datasets(self) -> List[dict]:
        """Get datasets and their attribute order

        Raises:
            PureAUTHApiError: API error

        Returns:
            List[dict]: Returns a list of datasets. e.g.
                [{'attributes': [{'name': 'Full Name', 'order': 1, 'type': 'string'},
                {'name': 'Corporate Email', 'order': 2, 'type': 'email'},
                {'name': 'Personal Email', 'order': 3, 'type': 'email'},
                {'name': 'Phone Number', 'order': 4, 'type': 'phone_number'}],
                'id': 3,
                'name': 'Primary',
                'public_id': '93258db8-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                'type': 'primary',
                'attrib_list': [{'name': 'Full Name'},
                {'name': 'Corporate Email'},
                {'name': 'Personal Email'},
                {'name': 'Phone Number'}]}]
        """
        try:
            res = requests.get(self.url.dataset_url(), headers=self.request_headers)
            data = res.json()
            datasets = None
            if data["status"] == "failure":
                error = data.get("user_error")
                raise DatasetListApiError(f"{res.status_code}: {error}")
            if data["status"] == "success":
                datasets = data["data"]["datasets"]
                return datasets
            else:
                raise DatasetListApiError(
                    "Could not get datasets. Something went wrong."
                )
        except Exception as e:
            raise PureAUTHApiError(e)

    def groups(self) -> List[dict]:
        """Gets all groups in your organization

        Raises:
            OrganizationGroupsApiError
            PureAUTHApiError

        Returns:
            List[dict]: List of group objects in form of a dictionary e.g.
            [   {'applications': 7,
                'description': 'All users in your organization.',
                'employees': 0,
                'name': 'Everyone',
                'public_id': 'cb60c9f8-cb3a-4726-a526-xxxxxxxxxxxx'}
            ]
        """
        try:
            res = requests.get(
                self.url.group_list_url(),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                groups = data["data"]
                return groups

            if data["status"] == "failure":
                raise OrganizationGroupsApiError(data.get("user_error"))
        except Exception as e:
            raise PureAUTHApiError(e)

    def roles(self) -> List[dict]:
        """Gets all roles in your organization.

        Raises:
            OrganizationGroupsApiError
            PureAUTHApiError

        Returns:
            List[dict]: List of role objects in form of a dictionary e.g.
            [{'applications': 0,
            'description': '',
            'employees': 9,
            'name': 'example_role',
            'public_id': 'bae2a890-0f44-4b16-8e80-xxxxxxxxxxxx'}]
        """
        try:
            res = requests.get(
                self.url.role_list_url(),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                roles = data["data"]
                return roles

            if data["status"] == "failure":
                raise OrganizationGroupsApiError(data.get("user_error"))
        except Exception as e:
            raise PureAUTHApiError(e)

    def fetch_logs(self) -> List[LogsDTO]:
        """Get logs for your organization

        Raises:
            OrganizationLogsApiError
            PureAUTHApiError

        Returns:
            List[LogsDTO]: List of LogsDTO dataclass objects.
        """
        try:
            res = requests.get(
                self.url.fetch_logs_url(),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                logs: List[LogsDTO] = []
                records = data.get("data", {}).get("records", [])
                for record in records:
                    log = LogsDTO(
                        log_id=record.get("id"),
                        actor_id=record.get("actor", {}).get("id"),
                        actor_role=record.get("actor", {}).get("role"),
                        actor_deanonymized="",
                        created_at=record.get("created_at"),
                        event=record.get("event"),
                        ip_address=record.get("ip_address"),
                        message=record.get("message"),
                        outcome=record.get("outcome"),
                    )
                    logs.append(log)
                return logs
            if data["status"] == "failure":
                raise OrganizationLogsApiError(data.get("user_error"))
        except Exception as e:
            raise PureAUTHApiError(e)

    def fetch_logs_filtered(self, from_date: str, to_date: str) -> List[LogsDTO]:
        """Get logs between specific dates

        Args:
            from_date (str): dd/mm/yyyy
            to_date (str): dd/mm/yyyy

        Raises:
            OrganizationLogsDateFormatError
            OrganizationLogsApiError
            PureAUTHApiError

        Returns:
            List[LogsDTO]: List of LogsDTO dataclass objects.
        """
        try:
            try:
                dt1 = datetime.strptime(from_date, "%d/%m/%Y")
                dt2 = datetime.strptime(to_date, "%d/%m/%Y")
            except Exception as e:
                raise OrganizationLogsDateFormatError(e)
            res = requests.get(
                self.url.fetch_logs_url_filtered(from_date=dt1, to_date=dt2),
                headers=self.request_headers,
            )
            data = res.json()
            if data["status"] == "success":
                logs: List[LogsDTO] = []
                records = data.get("data", {}).get("records", [])
                for record in records:
                    log = LogsDTO(
                        log_id=record.get("id"),
                        actor_id=record.get("actor", {}).get("id"),
                        actor_role=record.get("actor", {}).get("role"),
                        actor_deanonymized="",
                        created_at=record.get("created_at"),
                        event=record.get("event"),
                        ip_address=record.get("ip_address"),
                        message=record.get("message"),
                        outcome=record.get("outcome"),
                    )
                    logs.append(log)
                return logs
            if data["status"] == "failure":
                raise OrganizationLogsApiError(data.get("user_error"))
        except Exception as e:
            raise PureAUTHApiError(e)

    def _generate_emp_identifiers(self, corporate_emails: List[str]) -> Dict[str, str]:
        identifiers = {}
        for email in corporate_emails:
            # generating identifiers from email id and org email to map to employee email
            identifier = employee_id(self.config.organization_id, email)
            identifiers[identifier] = email
        return identifiers

    def deanonymize_logs(
        self, logs: List[LogsDTO], corporate_emails: List[str]
    ) -> List[LogsDTO]:
        """Deanonymize a list of logs using the provided corporate emails.

        Args:
            logs (List[LogsDTO]): List of LogsDTO objects to be deanonymized. WILL be modified
            corporate_emails (List[str]): List of corporate emails used for deanonymization.

        Returns:
            List[LogsDTO]: Modified LogsDTO objects with actor_deanonymized populated.
        """
        self.identifiers = self._generate_emp_identifiers(corporate_emails)
        deanonymized_logs = []
        for log in logs:
            if log.actor_role == "Admin":
                # If yes, set actor_deanonymized to actor_id as it's Admin
                log.actor_deanonymized = log.actor_id
            else:
                # Assign the de-anonymized actor_id to the actor_deanonymized attribute
                log.actor_deanonymized = self.identifiers.get(log.actor_id, "")

            # Append the de-anonymized log to the list
            deanonymized_logs.append(log)

        return deanonymized_logs
