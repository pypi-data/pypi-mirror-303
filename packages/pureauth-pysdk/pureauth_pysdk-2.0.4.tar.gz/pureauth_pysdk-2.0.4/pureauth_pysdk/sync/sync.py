from pureauth_pysdk.dto import PureAUTHServerConfigDTO

from .v1 import V1
from .v2 import V2


class Sync:
    def __init__(self, config: PureAUTHServerConfigDTO):
        self.config = config
        self.v1 = V1(config=config)
        self.v2 = V2(config=config)
