import unittest
from account import *


class TestCase(unittest.TestCase):

    def test_deposit(self):
        self.test_1 = Account('Jane')
        self.assertTrue(self.test_1.deposit(1000))
        self.assertEqual(self.test_1.get_balance(), 1000)
        self.test_2 = Account('Ben')
        self.assertFalse(self.test_2.deposit(-1000))
        self.assertEqual(self.test_2.get_balance(), 0)
        self.test_3 = Account('Will')
        self.assertFalse(self.test_3.deposit(0))
        self.assertEqual(self.test_3.get_balance(), 0)
        self.test_4 = Account('Walt')
        self.assertTrue(self.test_4.deposit(1000.50))
        self.assertAlmostEqual(self.test_4.get_balance(), 1000.50, delta=0.001)
        self.test_5 = Account('Hank')
        self.assertFalse(self.test_5.deposit(-1000.50))
        self.assertEqual(self.test_5.get_balance(), 0)
        with self.assertRaises(ValueError):
            self.test_5.deposit('x')

    def test_withdraw(self):
        self.t1 = Account('Jane')
        self.t1.deposit(1000)
        self.assertFalse(self.t1.withdraw(0))
        self.assertFalse(self.t1.withdraw(-1000))
        self.assertTrue(self.t1.withdraw(100))
        self.assertEqual(self.t1.get_balance(), 900)
        self.assertTrue(self.t1.withdraw(100.50))
        self.assertAlmostEqual(self.t1.get_balance(), 799.50, delta=0.001)
        self.assertTrue(self.t1.withdraw(799.50))
        self.assertEqual(self.t1.get_balance(), 0)
        with self.assertRaises(ValueError):
            self.t1.withdraw('x')

    def test_init(self):
        self.account_1 = Account('Chase')
        self.assertEqual(self.account_1.get_name(), 'Chase')
        self.assertEqual(self.account_1.get_balance(), 0)
        self.account_2 = Account(1)
        self.assertEqual(self.account_2.get_name(), '1')
        self.assertEqual(self.account_2.get_balance(), 0)

    if __name__ == '__main__':
        unittest.main()
