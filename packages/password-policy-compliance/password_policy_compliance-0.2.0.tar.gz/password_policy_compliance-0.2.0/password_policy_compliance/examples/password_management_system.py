import datetime
from password_policy_compliance import (
    password_validator,
    policy_compliance,
    password_strength,
    password_expiration,
    compliance_reporter,
)

class PasswordManagementSystem:
    def __init__(self, policy_name="STRONG"):
        self.policy = policy_compliance.get_policy(policy_name)
        self.expiration_policy = password_expiration.PasswordExpirationPolicy(
            expiration_days=90, warning_days=14
        )
        self.user_passwords = {}  # In a real system, this would be a database
        self.strength_threshold = 50 if policy_name == "NIST" else 70

    def set_password(self, username, password):
        validation_result = password_validator.validate_password(password, self.policy)
        if not validation_result["valid"]:
            print("Password does not meet policy requirements:")
            for error in validation_result["errors"]:
                print(f"- {error}")
            return False

        strength_result = password_strength.calculate_password_strength(password)
        if strength_result["score"] < self.strength_threshold:
            print(f"Password is too weak. Strength score: {strength_result['score']}/100")
            return False

        self.user_passwords[username] = {
            "password": password,
            "set_date": datetime.datetime.now(),
        }
        print(f"Password set successfully for user {username}")
        return True

    def check_password(self, username, password):
        if username not in self.user_passwords:
            print("User not found")
            return False

        user_data = self.user_passwords[username]
        if user_data["password"] != password:
            print("Incorrect password")
            return False

        if self.expiration_policy.is_password_expired(user_data["set_date"]):
            print("Password has expired. Please set a new password.")
            return False

        if self.expiration_policy.should_warn_user(user_data["set_date"]):
            days_left = self.expiration_policy.days_until_expiration(user_data["set_date"])
            print(f"Warning: Your password will expire in {days_left} days.")

        print("Login successful")
        return True

    def generate_compliance_report(self):
        passwords = [data["password"] for data in self.user_passwords.values()]
        report = compliance_reporter.generate_compliance_report(passwords, self.policy)
        print("Compliance Report:")
        print(f"Total passwords: {report['total_passwords']}")
        print(f"Compliant passwords: {report['compliant_passwords']}")
        print(f"Non-compliant passwords: {report['non_compliant_passwords']}")
        print(f"Compliance rate: {report['compliance_rate']}%")
        return report

# Usage example
if __name__ == "__main__":
    pms = PasswordManagementSystem()

    # Set passwords for users
    pms.set_password("alice", "Weak123")  # This should fail
    pms.set_password("alice", "Str0ngP@ssw0rd!")  # This should succeed
    pms.set_password("bob", "An0therStr0ngP@ss")

    # Check passwords
    pms.check_password("alice", "WrongPassword")  # This should fail
    pms.check_password("alice", "Str0ngP@ssw0rd!")  # This should succeed

    # Generate compliance report
    pms.generate_compliance_report()

    # Simulate password expiration
    pms.user_passwords["bob"]["set_date"] = datetime.datetime.now() - datetime.timedelta(days=100)
    pms.check_password("bob", "An0therStr0ngP@ss")  # This should warn about expiration
