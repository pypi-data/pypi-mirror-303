import re
from .policy_compliance import Policy
from datetime import datetime
from .password_strength import get_crack_time_estimation

def validate_password(password: str, policy: Policy, password_set_date: datetime = None) -> dict:
    """
    Validate a password against the given policy.
    
    Args:
    password (str): The password to validate
    policy (Policy): The policy to validate against
    password_set_date (datetime, optional): The date when the password was set or last changed

    Returns:
    dict: A dictionary containing validation results, any error messages, and crack time estimation
    """
    results = {
        "valid": True,
        "errors": []
    }
    
    # Check length
    if len(password) < policy.min_length:
        results["valid"] = False
        results["errors"].append(f"Password must be at least {policy.min_length} characters long")
    
    # Check complexity
    if policy.require_uppercase:
        if not any(c.isupper() for c in password[1:]):
            results["valid"] = False
            results["errors"].append("Password must contain at least one uppercase letter (not counting the first character)")
    
    if policy.require_lowercase:
        if not any(c.islower() for c in password[1:]):
            results["valid"] = False
            results["errors"].append("Password must contain at least one lowercase letter (not counting the first character)")
    
    if policy.require_digits:
        if not any(c.isdigit() for c in password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one digit")
    
    if policy.require_special:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one special character")
    
    # Check expiration
    if policy.expiration_policy and password_set_date:
        if policy.expiration_policy.is_password_expired(password_set_date):
            results["valid"] = False
            results["errors"].append("Password has expired")
        elif policy.expiration_policy.should_warn_user(password_set_date):
            days_left = policy.expiration_policy.days_until_expiration(password_set_date)
            results["warnings"] = [f"Password will expire in {days_left} days"]

    # Add crack time estimation
    results["crack_time_estimation"] = get_crack_time_estimation(password)

    return results
