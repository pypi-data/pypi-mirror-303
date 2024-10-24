# Changelog

All notable changes to the Password Policy Compliance Library will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2023-07-24

### Added
- Password expiration management functionality
- Blacklist checking feature (local and HaveIBeenPwned integration)
- Password generation capability
- Comprehensive User Guide (USER_GUIDE.md)
- More detailed examples in README.md

### Changed
- Improved password strength assessment using zxcvbn
- Enhanced crack time estimation
- Updated predefined policies to include more industry standards
- Refactored PasswordManagementSystem class for better flexibility

### Fixed
- Issues with password validation in edge cases
- Bugs in compliance reporting

## [0.1.5] - 2023-07-10

### Added
- Initial release of the Password Policy Compliance Library
- Basic password validation functionality
- Predefined policies (NIST, PCI DSS)
- Simple strength assessment
- Basic compliance reporting

[0.2.0]: https://github.com/bassemabidi/password_policy_compliance/compare/v0.1.5...v0.2.0
[0.1.5]: https://github.com/bassemabidi/password_policy_compliance/releases/tag/v0.1.5
