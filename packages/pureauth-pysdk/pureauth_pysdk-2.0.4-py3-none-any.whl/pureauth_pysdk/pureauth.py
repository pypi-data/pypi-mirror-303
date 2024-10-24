from .dto import PureAUTHServerConfigDTO
from .errors import AccessTokenValidationError
from .sync import Sync


class Pureauth:
    def __init__(
        self,
        organization_id: str,
        access_token: str,
        base_url: str = "https://live.pureauth.io",
        private_key: str = None,
    ):
        api_version = "v1"  # Force v1 until v2 is complete.
        self.config = PureAUTHServerConfigDTO(
            organization_id=organization_id,
            access_token=access_token,
            base_url=base_url if base_url[-1] != "/" else base_url[:-1],
            api_version=api_version,
            private_key=private_key,
        )
        self.validate_accesstoken()
        self.sync = Sync(config=self.config)

    def validate_accesstoken(self) -> bool:
        # raise AccessTokenValidationError
        pass
