import json
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from .errors import EmployeeDTOMissingDataError

from pureauth_pysdk.dto import PureAUTHServerConfigDTO


class ApiUri:
    def __init__(self, config: PureAUTHServerConfigDTO):
        self.base_url = config.base_url
        self.api_version = config.api_version
        self.api_base = f"{config.base_url}/api/v2"

    def employee_add_url(self) -> str:
        return f"{self.api_base}/employees/"

    def employee_status_url(self) -> str:
        return f"{self.api_base}/employees/status"

    def employee_activate_url(self) -> str:
        return f"{self.api_base}/employees/activate"

    def employee_deactivate_url(self) -> str:
        return f"{self.api_base}/employees/deactivate"

    def employee_update_url(self) -> str:
        return f"{self.api_base}/employees/"

    def employee_group_attach_url(self) -> str:
        return f"{self.api_base}/employees/groups/"

    def employee_signature_url(self) -> str:
        return f"{self.api_base}/employees/signatures"

    def employee_autoosm_fetch_url(self) -> str:
        return f"{self.api_base}/employees/fetch-auto-osm"

    def employee_role_attach_url(self) -> str:
        return f"{self.api_base}/employees/roles/"

    def welcome_email_url(self) -> str:
        return f"{self.api_base}/employees/welcome"

    # TEMP V1 URLS
    def public_key_upload_url(self) -> str:
        return f"{self.base_url}/api/v1/organizations/publickey"

    def fetch_csv_url(self) -> str:
        return f"{self.base_url}/api/v1/organizations/datasets/csv-template"

    def dataset_url(self) -> str:
        return f"{self.base_url}/api/v1/organizations/datasets/?include=all"

    def group_list_url(self) -> str:
        return f"{self.base_url}/api/v1/organizations/groups"

    def role_list_url(self) -> str:
        return f"{self.base_url}/api/v1/organizations/roles"

    def fetch_logs_url(self) -> str:
        return f"{self.base_url}/api/v1/audit_logs/"

    def fetch_logs_url_filtered(self, from_date: datetime, to_date: datetime) -> str:
        d1 = from_date.strftime("%d/%m/%Y")
        d2 = to_date.strftime("%d/%m/%Y")
        return (
            f"{self.base_url}/api/v1/audit_logs/?from_date={d1}&to_date={d2}&order=desc"
        )


@dataclass
class PrimaryDatasetMappingDTO:
    full_name: str = "Full Name"
    primary_email: str = "Personal Email"
    corporate_email: str = "Corporate Email"
    phone_number: str = "Phone Number"


@dataclass(init=False, repr=True, eq=True)
class EmployeePrimaryDatasetDTO:
    full_name: str
    primary_email: str
    corporate_email: str
    phone_number: str
    user_dataset: dict

    def __init__(
        self,
        full_name: str = "",
        primary_email: str = "",
        corporate_email: str = "",
        phone_number: str = "",
        mapping: PrimaryDatasetMappingDTO = PrimaryDatasetMappingDTO(),
    ):
        # Validate all data exists
        if not full_name:
            raise EmployeeDTOMissingDataError(
                "Missing required dataset attribute: full_name"
            )
        if not primary_email:
            raise EmployeeDTOMissingDataError(
                "Missing required dataset attribute: primary_email"
            )
        if not corporate_email:
            raise EmployeeDTOMissingDataError(
                "Missing required dataset attribute: corporate_email"
            )
        if not phone_number:
            raise EmployeeDTOMissingDataError(
                "Missing required dataset attribute: phone_number"
            )
        # Normalize data
        self.full_name = full_name.lower().strip()
        self.primary_email = primary_email.lower().strip()
        self.corporate_email = corporate_email.lower().strip()
        self.phone_number = (
            phone_number.lower().strip().replace("-", "").replace(" ", "")
        )
        self.user_dataset = {
            mapping.full_name: self.full_name,
            mapping.corporate_email: self.corporate_email,
            mapping.primary_email: self.primary_email,
            mapping.phone_number: self.phone_number,
        }


@dataclass(init=False, repr=True, eq=True)
class EmployeeSecondaryDatasetDTO:
    username: str
    user_principal_name: str
    employee_id: str
    object_id: str
    employee_type: str
    otherattribute1: dict

    def __init__(
        self,
        username: str = "",
        user_principal_name: str = "",
        employee_id: str = "",
        object_id: str = "",
        employee_type: str = "",
        otherattribute1: str = "",
    ) -> None:
        self.username = username if username is not None else ""
        self.user_principal_name = (
            user_principal_name if user_principal_name is not None else ""
        )
        self.employee_id = employee_id if employee_id is not None else ""
        self.object_id = object_id if object_id is not None else ""
        self.employee_type = employee_type if employee_type is not None else ""
        self.otherattribute1 = otherattribute1 if otherattribute1 is not None else ""
        self.serialized = json.dumps(
            OrderedDict(
                [
                    ("Username", self.username),
                    ("UserPrincipalName", self.user_principal_name),
                    ("EmployeeID", self.employee_id),
                    ("ObjectID", self.object_id),
                    ("EmployeeType", self.employee_type),
                    ("OtherAttribute1", self.otherattribute1),
                ]
            )
        )


@dataclass(init=False, repr=True, eq=True)
class EmployeeAccessMappingDTO:
    corporate_email: str
    groups: List[str] = field(default_factory=list)
    roles: List[str] = field(default_factory=list)

    def __init__(
        self, corporate_email: str, groups: List[str] = [], roles: List[str] = []
    ):
        self.corporate_email = corporate_email.strip().lower()
        self.groups = []
        self.roles = []
        for group in groups:
            self.groups.append(group.strip().lower())
        for role in roles:
            self.roles.append(role.strip().lower())


@dataclass
class EmployeeDatasetDTO:
    primary_dataset: EmployeePrimaryDatasetDTO
    secondary_dataset: EmployeeSecondaryDatasetDTO
    mapping_dataset: EmployeeAccessMappingDTO


@dataclass
class LogsDTO:
    log_id: str
    actor_id: str
    actor_role: str
    actor_deanonymized: str
    created_at: str
    event: str
    ip_address: str
    message: str
    outcome: str
