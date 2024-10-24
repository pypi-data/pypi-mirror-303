import unittest
from datetime import datetime, timedelta
from password_policy_compliance.examples.password_management_system import PasswordManagementSystem

class TestPasswordManagementSystem(unittest.TestCase):
    def setUp(self):
        self.pms = PasswordManagementSystem(policy_name="NIST")  # Using NIST policy for less strict requirements

    def test_set_password_valid(self):
        result = self.pms.set_password("alice", "Str0ngP@ssw0rd!")
        self.assertTrue(result)
        self.assertIn("alice", self.pms.user_passwords)

    def test_set_password_invalid(self):
        result = self.pms.set_password("bob", "weak")
        self.assertFalse(result)
        self.assertNotIn("bob", self.pms.user_passwords)

    def test_check_password_correct(self):
        self.pms.set_password("charlie", "An0therStr0ngP@ss")
        result = self.pms.check_password("charlie", "An0therStr0ngP@ss")
        self.assertTrue(result)

    def test_check_password_incorrect(self):
        self.pms.set_password("david", "Str0ngP@ssw0rd!")
        result = self.pms.check_password("david", "WrongPassword")
        self.assertFalse(result)

    def test_password_expiration(self):
        # First, set a valid password for 'eve'
        result = self.pms.set_password("eve", "Str0ngP@ssw0rd123!")
        print(f"Password set result for 'eve': {result}")
        print(f"Current user_passwords: {self.pms.user_passwords}")
        
        # Verify that 'eve' is in the user_passwords dictionary
        self.assertIn("eve", self.pms.user_passwords)
        
        # Manually set the password set date to 100 days ago
        self.pms.user_passwords["eve"]["set_date"] = datetime.now() - timedelta(days=100)
        
        # Now check the password
        result = self.pms.check_password("eve", "Str0ngP@ssw0rd123!")
        print(f"Check password result for 'eve': {result}")
        
        # The result should be False because the password has expired
        self.assertFalse(result)

    def test_generate_compliance_report(self):
        self.pms.set_password("user1", "Str0ngP@ssw0rd!")
        self.pms.set_password("user2", "An0therStr0ngP@ss")
        self.pms.set_password("user3", "YetAn0therStr0ngP@ss")
        report = self.pms.generate_compliance_report()
        self.assertIsNotNone(report)
        self.assertEqual(report['total_passwords'], 3)
        self.assertEqual(report['compliant_passwords'], 3)
        self.assertEqual(report['compliance_rate'], 100.0)

if __name__ == '__main__':
    unittest.main()
