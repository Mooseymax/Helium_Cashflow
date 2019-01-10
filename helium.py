import csv
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl import load_workbook

class Account:
    def __init__(self, name, type, value, growth, p_cost, m_cost):
        self.n = name
        self.t = type
        self.v = value
        self.g = growth
        self.pc = p_cost    # Percentage cost
        self.mc = m_cost    # Monatary cost
        self.transactions = []
        
    def add_transaction(self, transaction):
        t = transaction
        self.transactions.append(t)
        print('Added Transaction')
    
class Transaction:
    def __init__(self, name, type, amount, direction, freq, start, end):
        self.n = name
        self.t = type
        self.a = amount
        self.d = direction
        self.f = freq
        self.s = start
        self.e = end

class MarketEvent:
    def __init__(self, name, date, movement):
        self.n = name
        self.d = date
        self.m = movement

def projection:
    
accounts = []
transactions = []
events = []

''' Example '''
e_account = Account('Narendra AJ Bell Investcentre SIPP', 'Pension', 100000, 0.045, 0.00, 2000)

print(e_account.n)
