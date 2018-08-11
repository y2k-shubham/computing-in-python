import datetime
import time


# Definition of BankAccount_1
class BankAccount_1:

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self._log("Account created with balance {}".format(balance))

    def get_balance(self):
        self._log("Balanced checked at {}".format(self.balance))
        return self.balance

    def set_balance(self, new_balance):
        self._log("Balance set at {}".format(new_balance))
        self.balance = new_balance

    def _log(self, msg):
        log_filename = 'log-file-{}.txt'.format(self.name)
        with open(log_filename, 'a') as log_file:
            log_msg = "{}\t{}".format(self._get_timestamp(), msg)
            print(log_msg, file=log_file)

    @staticmethod
    def _get_timestamp():
        return datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")


# Demo of BankAccount_1
bank_account_amar = BankAccount_1(name="Amar", balance=25000)
time.sleep(1)
bank_account_ruchi = BankAccount_1(name="Ruchi")
time.sleep(1)

print(bank_account_amar.get_balance())
time.sleep(1)
bank_account_ruchi.set_balance(new_balance=12000)
time.sleep(1)

bank_account_amar.set_balance(new_balance=32000)
time.sleep(1)
bank_account_ruchi.get_balance()


#############################

# Definition of BankAccount_2
class BankAccount_2:
    min_balance = 1000

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self._log("Account created with balance {}".format(balance))

    def get_balance(self):
        self._log("Balanced checked at {}".format(self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self._log("Deposit amount = {}, updated balance = {}".format(amount, self.balance))

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance >= self.min_balance:
            self.balance = new_balance
            self._log("Withdraw amount = {}, updated balance = {}".format(amount, self.balance))
        else:
            self._log("Withdraw amount = {}, rejected!".format(amount))

    def _log(self, msg):
        log_filename = 'log-file-{}.txt'.format(self.name)
        with open(log_filename, 'a') as log_file:
            log_msg = "{}\t{}".format(self._get_timestamp(), msg)
            print(log_msg, file=log_file)

    @staticmethod
    def _get_timestamp():
        return datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")


# Demo of BankAccount_1
bank_account_avinash = BankAccount_2(name="Avinash", balance=21000)
time.sleep(1)
bank_account_rupali = BankAccount_2(name="Rupali", balance=17000)
time.sleep(1)

bank_account_avinash.withdraw(amount=3227)
bank_account_avinash.withdraw(amount=1771)
time.sleep(1)
bank_account_rupali.deposit(amount=1355)
bank_account_rupali.get_balance()
time.sleep(1)
bank_account_avinash.deposit(amount=9875)
bank_account_rupali.get_balance()
bank_account_rupali.deposit(amount=4100)
time.sleep(1)
time.sleep(1)
bank_account_rupali.get_balance()
bank_account_avinash.withdraw(amount=82000)
time.sleep(1)
bank_account_avinash.get_balance()
time.sleep(1)
bank_account_rupali.get_balance()
