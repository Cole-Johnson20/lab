import pytest
from account import *


class Test:
    def setup_method(self):
        self.test_1 = Account('Jane')
        self.test_2 = Account('Ben')
        self.test_3 = Account('Will')
        self.test_4 = Account('Walt')
        self.test_5 = Account('Hank')
        self.test_6 = Account('Jane')
        self.test_7 = Account('Chase')
        self.test_8 = Account(1)

    def teardown_method(self):
        del self.test_1
        del self.test_2
        del self.test_3
        del self.test_4
        del self.test_5
        del self.test_6
        del self.test_7

    def test_deposit(self):
        assert self.test_1.deposit(1000) is True
        assert self.test_1.get_balance() == 1000

        assert self.test_2.deposit(-1000) is False
        assert self.test_2.get_balance() == 0

        assert self.test_3.deposit(0) is False
        assert self.test_3.get_balance() == 0

        assert self.test_4.deposit(1000.50) is True
        assert self.test_4.get_balance() == 1000.50

        assert self.test_5.deposit(-1000.50) is False
        assert self.test_5.get_balance() == 0

        with pytest.raises(TypeError):
            self.test_5.deposit('x')

    def test_withdraw(self):
        self.test_6.deposit(1000)
        assert self.test_6.withdraw(0) is False
        assert self.test_6.withdraw(-1000) is False
        assert self.test_6.withdraw(100) is True
        assert self.test_6.get_balance() == 900
        assert self.test_6.withdraw(100.50) is True
        assert self.test_6.get_balance() == 799.50
        assert self.test_6.withdraw(799.50) is True
        assert self.test_6.get_balance() == 0

        with pytest.raises(TypeError):
            self.test_6.withdraw('x')

    def test_init(self):
        assert self.test_7.get_name() == 'Chase'
        assert self.test_7.get_balance() == 0
        assert self.test_8.get_name() == '1'
        assert self.test_8.get_balance() == 0
