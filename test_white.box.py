
import unittest
from white_box import BankingSystem, BankAccount

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.banking_system = BankingSystem()

    def test_authenticate_success(self):
        result = self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(result)

    def test_authenticate_failure_wrong_password(self):
        result = self.banking_system.authenticate("user123", "wrongpass")
        self.assertFalse(result)

    def test_authenticate_failure_nonexistent_user(self):
        result = self.banking_system.authenticate("nonexistent", "pass123")
        self.assertFalse(result)

    def test_transfer_money_success_regular(self):
        self.banking_system.authenticate("user123", "pass123")
        sender = "user123"
        receiver = "receiver123"
        amount = 100
        transaction_type = "regular"
        result = self.banking_system.transfer_money(sender, receiver, amount, transaction_type)
        self.assertTrue(result)

    def test_transfer_money_failure_insufficient_funds(self):
        self.banking_system.authenticate("user123", "pass123")
        sender = "user123"
        receiver = "receiver123"
        amount = 2000  # Exceeds balance
        transaction_type = "regular"
        result = self.banking_system.transfer_money(sender, receiver, amount, transaction_type)
        self.assertFalse(result)

    def test_transfer_money_failure_invalid_transaction_type(self):
        self.banking_system.authenticate("user123", "pass123")
        sender = "user123"
        receiver = "receiver123"
        amount = 100
        transaction_type = "invalid_type"
        result = self.banking_system.transfer_money(sender, receiver, amount, transaction_type)
        self.assertFalse(result)

    def test_transfer_money_failure_sender_not_authenticated(self):
        sender = "user123"
        receiver = "receiver123"
        amount = 100
        transaction_type = "regular"
        result = self.banking_system.transfer_money(sender, receiver, amount, transaction_type)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()