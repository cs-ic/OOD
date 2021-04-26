"""

class ShoppingCart:
    
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += (quantity*price)
        self.items.update({item_name : quantity})

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity*price)
        self.items[item_name] -= quantity
        if self.items[item_name] == 0: del self.items[item_name]
    
    def checkout(self, cash_paid):
        if self.total == cash_paid:
            return ('Thank you for shoping with us!!!')
        elif cash_paid < self.total:
            self.checkout(int(input(f"You are {self.total - cash_paid} short after paying {cash_paid}. Repay the amount : ")))
        else: 
            return (f"Here's your balance {cash_paid - self.total}$. Thank you for shoping with us!!!!")



cart = ShoppingCart()

cart.add_item('A', 10, 50)
cart.add_item('B', 5, 20)

cart.remove_item('B', 1, 20)

cart_res = cart.checkout(500)

print('Total cart amount:', cart.total)
print('Cart items:', cart.items)

print(cart_res)

"""

"""
# Encapsulation : to hide the data from runtime enviorment and make it accesible only via funcitons\

class Product:
    def __init__(self):
        self.max_price = 900
    
    def sell(self):
        print("Selling Price :", self.max_price)
    
    def set_max_price(self,price):
        self.max_price = price

product = Product()
product.sell()

# change the price
product.__maxprice = 1000
product.sell()

# using setter function
product.set_max_price(1000)
product.sell()

"""
"""
from abc import ABC, abstractmethod

class Parent(ABC):
    def common(self):
        print("In common class method of Parent")

    @abstractmethod
    def vary(self):
        pass

class Child1(Parent):
    def vary(self):
        print("In vary class of child1")
    
class Child2(Parent):
    def vary(self):
        print("In vary class of child2")

# object of Child1 class
child1 = Child1()
child1.common()
child1.vary()

# object of Child2 class
child2 = Child2()
child2.common()
child2.vary()
    
"""

"""
class Person:

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):

    def is_employee(self):
        return True

# Driver code
emp = Person("Person 1")
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))

emp = Employee("Employee 1")
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))
"""