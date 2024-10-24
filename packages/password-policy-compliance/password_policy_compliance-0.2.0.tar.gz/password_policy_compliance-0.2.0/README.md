# Password Policy Compliance Library

A Python library that helps enforce password policies, ensuring password compliance with best practices and industry standards.

## Features

- Password validation against customizable security policies
- Pre-defined policies based on industry standards (NIST, PCI DSS, HIPAA, SOX, GDPR)
- Custom policy creation
- Password expiration management
- Compliance reporting and auditing
- Password strength assessment using zxcvbn
- Crack time estimation
- Blacklist checking (local and HaveIBeenPwned integration)
- Password generation

## Installation

To install the Password Policy Compliance Library, run:

```
pip install password-policy-compliance
```

## Quick Start

Here's a quick example of how to use the library with a predefined policy:

```python
from password_policy_compliance import password_validator, policy_compliance, password_strength

# Get a predefined policy
nist_policy = policy_compliance.get_policy("NIST")

# Validate a password
password = "MyStr0ngP@ssw0rd"
result = password_validator.validate_password(password, nist_policy)

if result["valid"]:
    print(f"Password '{password}' is valid according to NIST policy!")
    strength_result = password_strength.calculate_password_strength(password)
    print(f"Password strength score: {strength_result['score']}/100")
    print("Estimated crack times:")
    for scenario, time in strength_result["crack_times_display"].items():
        print(f"  {scenario}: {time}")
else:
    print(f"Password '{password}' is invalid. Errors:")
    for error in result["errors"]:
        print(f"- {error}")

# Create a custom policy
custom_policy = policy_compliance.create_policy(
    name="Custom",
    min_length=12,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True,
    expiration_days=90,
    warning_days=14
)

# Validate against custom policy
result = password_validator.validate_password(password, custom_policy)
print(f"Password valid for custom policy: {result['valid']}")
```

## Documentation

For detailed information on how to use all features of the Password Policy Compliance Library, please refer to our [User Guide](USER_GUIDE.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Bassem Abidi (abidi.bassem@me.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
