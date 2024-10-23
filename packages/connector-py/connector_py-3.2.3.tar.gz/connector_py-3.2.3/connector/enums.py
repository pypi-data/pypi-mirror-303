import enum


class ActivityEventType(str, enum.Enum):
    LAST_LOGIN = "LastLogin"
    LAST_ACTIVITY = "LastActivity"


class CustomAttributeType(str, enum.Enum):
    STRING = "STRING"
    USER = "USER"


class CustomAttributeCustomizedType(str, enum.Enum):
    ACCOUNT = "ACCOUNT"
    ENTITLEMENMT = "ENTITLEMENT"
    RESOURCE = "RESOURCE"


class AccountStatus(str, enum.Enum):
    """
    This is a subset of the statuses supported by Lumos.
    """

    # The account has an active access to the system.
    ACTIVE = "ACTIVE"
    # The account can't access the system is suspended, but they can be reactivated.
    SUSPENDED = "SUSPENDED"
    # The account is deleted in the system but the user data is kept for future reference.
    DEPROVISIONED = "DEPROVISIONED"
    PENDING = "PENDING"
