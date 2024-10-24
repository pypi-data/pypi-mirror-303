import unittest
from password_policy_compliance.policy_compliance import get_policy, create_policy, Policy

class TestPolicyCompliance(unittest.TestCase):
    def test_get_predefined_policy(self):
        nist_policy = get_policy("NIST")
        self.assertIsInstance(nist_policy, Policy)
        self.assertEqual(nist_policy.name, "NIST SP 800-63B")

    def test_create_custom_policy(self):
        custom_policy = create_policy(
            name="Custom",
            min_length=10,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True,
            expiration_days=60,
            warning_days=7
        )
        self.assertIsInstance(custom_policy, Policy)
        self.assertEqual(custom_policy.name, "Custom")
        self.assertEqual(custom_policy.min_length, 10)
        self.assertTrue(custom_policy.require_uppercase)
        self.assertTrue(custom_policy.require_lowercase)
        self.assertTrue(custom_policy.require_digits)
        self.assertTrue(custom_policy.require_special)
        self.assertIsNotNone(custom_policy.expiration_policy)

    def test_get_invalid_policy(self):
        with self.assertRaises(ValueError):
            get_policy("INVALID_POLICY")

if __name__ == '__main__':
    unittest.main()
