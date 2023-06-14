import pytest
from app.calculations import add,subtract,multiply,divide, BankAccount, InsuficientFunds

@pytest.fixture
def bank_account():
    print("Creating bank account with 50 balance")
    return BankAccount(50)

@pytest.fixture
def default_bank_account():
    print("Creating empty bank account")
    return BankAccount(0)

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2, 5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1,num2,expected):
    print("Testing add function")
    assert add(num1,num2) == expected

def test_subtract():
    print("Testing substract function")
    assert subtract(9,4) == 5

def test_multiply():
    print("Testing substract function")
    assert multiply(4,3) == 12

def test_divide():
    print("Testing substract function")
    assert divide(20,4) == 5

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50


def test_bank_set_default_amount(default_bank_account):
    assert default_bank_account.balance == 0

def test_bank_set_withdraw_amount(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_bank_set_deposit_amount(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55



@pytest.mark.parametrize("deposited, withdrew, expected",[
    (200,100,100),
    (50,10,40),
    (1200,200,1000),
])
def test_bank_transaction(default_bank_account, deposited, withdrew, expected):
    default_bank_account.deposit(deposited)
    default_bank_account.withdraw(withdrew)
    assert default_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsuficientFunds):
        bank_account.withdraw(200)