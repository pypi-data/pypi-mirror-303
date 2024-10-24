from dataclasses import dataclass


@dataclass
class PureAUTHServerConfigDTO:
    access_token: str
    organization_id: str
    base_url: str
    api_version: str
    private_key: None
