from dataclasses import dataclass
from .password_expiration import PasswordExpirationPolicy

@dataclass
class Policy:
    name: str
    min_length: int
    require_uppercase: bool
    require_lowercase: bool
    require_digits: bool
    require_special: bool
    expiration_policy: PasswordExpirationPolicy = None

def create_policy(name: str, min_length: int, require_uppercase: bool, require_lowercase: bool,
                  require_digits: bool, require_special: bool, 
                  expiration_days: int = None, warning_days: int = None) -> Policy:
    """
    Create a password policy.

    Args:
    name (str): Name of the policy
    min_length (int): Minimum length required for passwords
    require_uppercase (bool): Whether to require uppercase letters
    require_lowercase (bool): Whether to require lowercase letters
    require_digits (bool): Whether to require digits
    require_special (bool): Whether to require special characters
    expiration_days (int, optional): Number of days after which a password expires
    warning_days (int, optional): Number of days before expiration to start warning the user

    Returns:
    Policy: A Policy object with the specified requirements
    """
    expiration_policy = None
    if expiration_days is not None and warning_days is not None:
        expiration_policy = PasswordExpirationPolicy(expiration_days, warning_days)

    return Policy(
        name=name,
        min_length=min_length,
        require_uppercase=require_uppercase,
        require_lowercase=require_lowercase,
        require_digits=require_digits,
        require_special=require_special,
        expiration_policy=expiration_policy
    )

# Pre-defined policies
NIST_POLICY = create_policy(
    name="NIST SP 800-63B",
    min_length=8,
    require_uppercase=False,
    require_lowercase=False,
    require_digits=False,
    require_special=False,
    expiration_days=None,  # NIST recommends against mandatory periodic password changes
    warning_days=None
)

PCI_DSS_POLICY = create_policy(
    name="PCI DSS",
    min_length=7,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=90,
    warning_days=14
)

HIPAA_POLICY = create_policy(
    name="HIPAA",
    min_length=8,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=60,
    warning_days=14
)

SOX_POLICY = create_policy(
    name="SOX",
    min_length=8,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=90,
    warning_days=14
)

GDPR_POLICY = create_policy(
    name="GDPR",
    min_length=10,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=None,  # GDPR doesn't specify password expiration
    warning_days=None
)

STRONG_POLICY = create_policy(
    name="Strong",
    min_length=12,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=90,
    warning_days=14
)

# Dictionary of all pre-defined policies
PREDEFINED_POLICIES = {
    "NIST": NIST_POLICY,
    "PCI_DSS": PCI_DSS_POLICY,
    "HIPAA": HIPAA_POLICY,
    "SOX": SOX_POLICY,
    "GDPR": GDPR_POLICY,
    "STRONG": STRONG_POLICY
}

def get_policy(policy_name: str) -> Policy:
    """
    Get a pre-defined policy by name.

    Args:
    policy_name (str): Name of the policy to retrieve

    Returns:
    Policy: The requested pre-defined policy

    Raises:
    ValueError: If the requested policy name is not found
    """
    policy = PREDEFINED_POLICIES.get(policy_name.upper())
    if policy is None:
        raise ValueError(f"Policy '{policy_name}' not found. Available policies: {', '.join(PREDEFINED_POLICIES.keys())}")
    return policy
