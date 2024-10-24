import pytest
from password_policy_compliance.policy_compliance import get_policy, PREDEFINED_POLICIES
from password_policy_compliance.password_validator import validate_password

@pytest.mark.parametrize("policy_name", PREDEFINED_POLICIES.keys())
def test_get_policy(policy_name):
    policy = get_policy(policy_name)
    assert policy.name == PREDEFINED_POLICIES[policy_name].name

def test_get_policy_invalid():
    with pytest.raises(ValueError):
        get_policy("INVALID_POLICY")

@pytest.mark.parametrize("policy_name, password, expected_valid", [
    ("NIST", "8charpass", True),  # NIST requires at least 8 characters
    ("NIST", "longerpassword", True),
    ("NIST", "short", False),  # This should fail as it's less than 8 characters
    ("PCI_DSS", "Aa1!abcd", True),
    ("PCI_DSS", "tooshort", False),
    ("HIPAA", "Aa1!abcd", True),
    ("HIPAA", "nouppercase1!", False),
    ("SOX", "Aa1!abcdefgh", True),
    ("SOX", "nospecialchar1A", False),
    ("GDPR", "Aa1!abcdefghijk", True),
    ("GDPR", "tooshort1!", False),
    ("STRONG", "Aa1!abcdefghijk", True),
    ("STRONG", "AlmostStrong1", False),
])
def test_validate_password_with_predefined_policies(policy_name, password, expected_valid):
    policy = get_policy(policy_name)
    result = validate_password(password, policy)
    assert result["valid"] == expected_valid, f"Failed for {policy_name} with password '{password}'"

@pytest.mark.parametrize("policy_name", PREDEFINED_POLICIES.keys())
def test_policy_attributes(policy_name):
    policy = get_policy(policy_name)
    assert isinstance(policy.min_length, int)
    assert isinstance(policy.require_uppercase, bool)
    assert isinstance(policy.require_lowercase, bool)
    assert isinstance(policy.require_digits, bool)
    assert isinstance(policy.require_special, bool)
    if policy.expiration_policy:
        assert isinstance(policy.expiration_policy.expiration_days, int)
        assert isinstance(policy.expiration_policy.warning_days, int)
