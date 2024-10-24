import unittest
from password_policy_compliance.blacklist_checker import is_password_blacklisted, check_haveibeenpwned, load_blacklist, is_password_secure

class TestBlacklistChecker(unittest.TestCase):
    def test_is_password_blacklisted(self):
        blacklist = {"password", "123456", "qwerty"}
        self.assertTrue(is_password_blacklisted("password", blacklist))
        self.assertFalse(is_password_blacklisted("securepassword", blacklist))

    def test_check_haveibeenpwned(self):
        self.assertTrue(check_haveibeenpwned("password"))
        self.assertFalse(check_haveibeenpwned("veryunlikelytobebreached12345!@#$%"))

    def test_is_password_secure(self):
        blacklist = {"password", "123456", "qwerty"}
        self.assertFalse(is_password_secure("password", blacklist))
        self.assertTrue(is_password_secure("veryunlikelytobebreached12345!@#$%", blacklist))

if __name__ == '__main__':
    unittest.main()
