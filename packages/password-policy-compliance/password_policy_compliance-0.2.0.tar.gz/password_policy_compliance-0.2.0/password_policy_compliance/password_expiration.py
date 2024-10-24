from datetime import datetime, timedelta

class PasswordExpirationPolicy:
    def __init__(self, expiration_days: int, warning_days: int):
        """
        Initialize a password expiration policy.

        Args:
        expiration_days (int): Number of days after which a password expires
        warning_days (int): Number of days before expiration to start warning the user
        """
        self.expiration_days = expiration_days
        self.warning_days = warning_days

    def is_password_expired(self, password_set_date: datetime) -> bool:
        """
        Check if a password has expired.

        Args:
        password_set_date (datetime): The date when the password was set or last changed

        Returns:
        bool: True if the password has expired, False otherwise
        """
        expiration_date = password_set_date + timedelta(days=self.expiration_days)
        return datetime.now() > expiration_date

    def days_until_expiration(self, password_set_date: datetime) -> int:
        """
        Calculate the number of days until the password expires.

        Args:
        password_set_date (datetime): The date when the password was set or last changed

        Returns:
        int: Number of days until expiration (negative if already expired)
        """
        expiration_date = password_set_date + timedelta(days=self.expiration_days)
        days_left = (expiration_date - datetime.now()).days
        return max(days_left, 0)

    def should_warn_user(self, password_set_date: datetime) -> bool:
        """
        Check if it's time to warn the user about password expiration.

        Args:
        password_set_date (datetime): The date when the password was set or last changed

        Returns:
        bool: True if it's time to warn the user, False otherwise
        """
        days_left = self.days_until_expiration(password_set_date)
        return 0 < days_left <= self.warning_days

def create_expiration_policy(expiration_days: int, warning_days: int) -> PasswordExpirationPolicy:
    """
    Create a new password expiration policy.

    Args:
    expiration_days (int): Number of days after which a password expires
    warning_days (int): Number of days before expiration to start warning the user

    Returns:
    PasswordExpirationPolicy: A new password expiration policy object
    """
    return PasswordExpirationPolicy(expiration_days, warning_days)
