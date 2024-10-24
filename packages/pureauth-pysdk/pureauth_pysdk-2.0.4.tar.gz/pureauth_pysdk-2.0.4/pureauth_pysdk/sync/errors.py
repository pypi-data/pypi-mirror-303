class PureAUTHApiError(Exception):
    pass


class DatasetListApiError(Exception):
    pass


class PublicKeyUploadApiError(Exception):
    pass


class DatasetCsvApiError(Exception):
    pass


class StatusApiError(Exception):
    pass


class DatasetFormatError(Exception):
    pass


class UserAddApiError(Exception):
    pass


class UserUpdateApiError(Exception):
    pass


class WelcomeEmailApiError(Exception):
    pass


class ActivateEmployeeApiError(Exception):
    pass


class DeactivateEmployeeApiError(Exception):
    pass


class OrganizationGroupsApiError(Exception):
    pass


class GroupAttachApiError(Exception):
    pass


class RoleAttachApiError(Exception):
    pass


class OrganizationLogsApiError(Exception):
    pass


class OrganizationLogsDateFormatError(Exception):
    pass


class JSONDecodeError(Exception):
    pass


class SignatureApiError(Exception):
    pass


class AutoOSMFetchApiError(Exception):
    pass
