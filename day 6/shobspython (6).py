# -*- coding: utf-8 -*-
"""shobspython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SrN7qghncZ7Aa4CN0AuHyapjEwE4m-WS
"""

class BankAccount:
 def __init__(self, forename, balance):
		self.forename = shobha
		my_account = forename
print('my_account')

class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
  
my_account = BankAccount(15)
my_account.deposit(5)
print(my_account.balance)