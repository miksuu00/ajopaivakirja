# transportation.py
class Vehicle:
    def __init__(self, make, power):
        self.make = make
        self.power = power
        self.expenses = []
        
    def add_expens(self, expense):
        self.expenses.append(expense)
        
class Expense:
    def __init__(self, date, description, cost, mileage):
        self.date = date
        self.description = description
        self.cost = cost
        self.mileage = mileage