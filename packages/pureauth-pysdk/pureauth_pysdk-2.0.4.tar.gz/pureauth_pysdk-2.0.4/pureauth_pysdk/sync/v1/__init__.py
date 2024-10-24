from pureauth_pysdk.dto import PureAUTHServerConfigDTO

from .employee import Employee
from .organization import Organization


class V1:
    def __init__(self, config: PureAUTHServerConfigDTO):
        self.config = config
        self.organization = Organization(self.config)
        self.employees = Employee(self.config, self.organization)
