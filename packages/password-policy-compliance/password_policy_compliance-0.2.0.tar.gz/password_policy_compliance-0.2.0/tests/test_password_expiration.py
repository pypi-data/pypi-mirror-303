import pytest
from datetime import datetime, timedelta
from password_policy_compliance.password_expiration import PasswordExpirationPolicy, create_expiration_policy
from password_policy_compliance.policy_compliance import create_policy
from password_policy_compliance.password_validator import validate_password

@pytest.fixture
def expiration_policy():
    return create_expiration_policy(expiration_days=90, warning_days=14)

@pytest.fixture
def test_policy(expiration_policy):
    return create_policy(
        name="Test",
        min_length=8,
        require_uppercase=True,
        require_lowercase=True,
        require_digits=True,
        require_special=True,
        expiration_days=90,
        warning_days=14
    )

def test_password_not_expired(expiration_policy):
    password_set_date = datetime.now() - timedelta(days=30)
    assert not expiration_policy.is_password_expired(password_set_date)

def test_password_expired(expiration_policy):
    password_set_date = datetime.now() - timedelta(days=100)
    assert expiration_policy.is_password_expired(password_set_date)

def test_days_until_expiration(expiration_policy):
    password_set_date = datetime.now() - timedelta(days=80)
    assert 0 < expiration_policy.days_until_expiration(password_set_date) <= 10

def test_should_warn_user(expiration_policy):
    password_set_date = datetime.now() - timedelta(days=80)
    assert expiration_policy.should_warn_user(password_set_date)

def test_validate_password_with_expiration(test_policy):
    password = "StrongP@ss1"
    
    # Test with a non-expired password
    result = validate_password(password, test_policy, datetime.now() - timedelta(days=30))
    assert result["valid"]
    assert "warnings" not in result
    assert "errors" not in result

    # Test with a password that will expire soon
    result = validate_password(password, test_policy, datetime.now() - timedelta(days=80))
    assert result["valid"]
    assert "warnings" in result
    assert "will expire in" in result["warnings"][0]

    # Test with an expired password
    result = validate_password(password, test_policy, datetime.now() - timedelta(days=100))
    assert not result["valid"]
    assert "errors" in result
    assert "Password has expired" in result["errors"]

def test_validate_password_without_expiration():
    policy_without_expiration = create_policy(
        name="No Expiration",
        min_length=8,
        require_uppercase=True,
        require_lowercase=True,
        require_digits=True,
        require_special=True
    )
    password = "StrongP@ss1"
    result = validate_password(password, policy_without_expiration)
    assert result["valid"]
    assert "warnings" not in result
    assert "errors" not in result
