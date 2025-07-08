#### Abstraction ####

# from abc import ABC, abstractmethod

# class Transport(ABC):

#     @abstractmethod
#     def travel(self):
#         pass

#     @abstractmethod
#     def info(self):
#         pass


# class Car(Transport):

#     def travel(self):
#         print("Traveling by car")
    
#     def info(self):
#         print("Car info")
    
#     def speed(self):
#         print("Car is fast running")


# c = Car()
# c.travel()
# c.info()
# c.speed()



#### Pattern strategy and Dependency injection ####


# class PaymentStrategy(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass


# class CreditCardPayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"Paying {amount} using Credit Card")
#         return "Paid with Credit Card"


# class ClickPayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"Paying {amount} using Click")
#         return "Paid with Click"

# class PayPalPayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"Paying {amount} using PayPal")
#         return "Paid with PayPal"


# class PaymePayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"Paying {amount} using Payme")
#         return "Paid with Payme"


# class Order:
#     def __init__(self, amount, strategy: PaymentStrategy):
#         self.amount = amount
#         self.strategy = strategy

    
#     def payment_proccess(self):
#         return self.strategy.pay(self.amount)


# order1 = Order(100, CreditCardPayment())
# order1.payment_proccess()

# order2 = Order(200, PaymePayment())
# order2.payment_proccess()

# order3 = Order(300, ClickPayment())
# order3.payment_proccess()


#### Inheritance ####


# class Transport:

#     transport_type = "Sigma"

#     def travel(self):
#         print(f"Trveling by transport")
#         return "Transport is traveling"

#     def info(self):
#         print(f"Transport info")
#         return "Transport info"


# class Car(Transport):
    
#     def info(self):
#         pass


# class Bus(Transport):

#     def info(self):
#         pass


# car = Car()
# car.travel()

# bus = Bus()
# bus.travel()

#### Class larda xotira boshqaruvi ####

# print(f"{id(Transport)=}") #4855267344
# print(f"{id(Car)=}") #4855268336
# print(f"{id(Bus)=}") #4855269328

# print(f"{id(car.travel())=}")
# print(f"{id(bus.travel())=}")

# print(f"{id(Transport.traveling_car)=}")
# print(f"{id(car.traveling_car)=}")

# bus.transport_type = "bus"

# print(Transport.transport_type)
# print(f"{id(Transport.transport_type)=}")
# print(bus.transport_type)
# print(f"{id(bus.transport_type)=}")
# print(f"{car.transport_type}")
# print(f"{id(car.transport_type)=}")


#### Class copy and deepcopy ####


# import copy

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person1 = Person("Fazliddin", 23)
# person2 = copy.copy(person1)

# print(f"{id(person1)=}")
# print(f"{id(person2)=}")

# print(f"{id(person1.name)=}")
# print(f"{id(person2.name)=}")

# person1 = Person("Fazliddin", [1,2,3])
# person2 = copy.copy(person1)

# person1.name = "dilshod"
# person1.age.append(4)

# print(f"{id(person1)=}")
# print(f"{id(person2)=}")

# print(f"{id(person1.name)=}")
# print(f"{id(person2.name)=}")


# print(f"{id(person1.age)=}")
# print(f"{id(person2.age)=}")




# person1 = Person("Fazliddin", [1,2,3])
# person2 = copy.deepcopy(person1)


# print(f"{id(person1)=}")
# print(f"{id(person2)=}")

# print(f"{id(person1.age)=}")
# print(f"{id(person2.age)=}")

# print(f"{id(person1.name)=}")
# print(f"{id(person2.name)=}")

# person2.name = "Dilshod"
# person2.age.append(4)


# print(f"{id(person1)=}")
# print(f"{id(person2)=}")

# print(f"{id(person1.age)=}")
# print(f"{id(person2.age)=}")

# print(f"{id(person1.name)=}")
# print(f"{id(person2.name)=}")



#### Method, classmethod and staticmethod ####



# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def gread(self):
#         print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
    
#     @classmethod
#     def from_string(cls, person_string):
#         name, age = person_string.split(", ")
#         return cls(name, age)
    
#     @staticmethod
#     def is_adult(age):
#         return age >= 18



#### Encapsulation ####


# class BankAccount:
#     available_currencies = ["UZB", "USD", "EUR"]

#     def __init__(self, account_number, balance):
#         self.account_number = account_number # public
#         self._currency_type = "USD" # protected
#         self.__balance = balance # private

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposit {amount}. New balance is {self.__balance}")
    
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficiant funds")
#         else:
#             self.__balance -= amount
#             print(f"Withdraw {amount}. New balance is {self.__balance}")
    
#     def get_currency_type(self):
#         print(self._currency_type)
    
#     def set_currency_type(self, currency_type):
#         if currency_type in self.available_currencies:
#             self._currency_type = currency_type
#         else:
#             raise ValueError("Invalid currency type")
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError("Balance cannot be negative.")
#         self.__balance = amount
    
#     @balance.deleter
#     def balance(self):
#         print("Deleting balance ...")
#         self.__balance = 0
    
#     def __str__(self):
#         return f"Account number :{self.account_number}, Balance {self.__balance}"


# bank_account = BankAccount("297492384671984", 500_000_000)

# print(bank_account.account_number)
# print(bank_account._currency_type)

# bank_account.account_number = "8274362834561"
# bank_account._currency_type = "UZB"

# print(bank_account.account_number)
# print(bank_account._currency_type)

# # print(bank_account.__balance)

# print(bank_account.__dict__)

# print(bank_account._BankAccount__balance)
# bank_account._BankAccount__balance = 2_000_000
# print(bank_account._BankAccount__balance)
# print("--------------------------------")

# print(bank_account.balance)
# bank_account.balance = 3000000
# print(bank_account.balance)
# del bank_account.balance
# print(bank_account.balance)
# bank_account.available_currencies.append("TJS")
# bank_account.set_currency_type("TJS")



###########################################################


#### Property and descriptor ####


# class IsmDescriptor:

#     def __get__(self, instance, owner):
#         print("Descriptor orqali o'qilyapti.")
#         return instance.__dict__["ism"]
    
#     def __set__(self, instance, value):
#         print("Descriptor orqali yozilyapti.")
#         instance.__dict__["ism"] = value


# class Talaba:
#     ism = IsmDescriptor()

#     def __init__(self, ism):
#         self._ism = ism


# talaba = Talaba("Fazliddin")
# print(talaba.ism)


##################################################

#### __new__, __init__ and type ####


# class MyClass:
#     pass

# obj = type("Talaba", (MyClass, ), {
#     "name": "Fazliddin",
#     "age": 21,
#     "info": lambda self: print("Hi")
# })

# print(obj().name)
# print(obj().age)
# obj().info()


# Transport = type("Transport", (), 
# {
#     "transport_type": "Transport",
#     "travel": lambda self: print(f"Traveling by transport."),
#     "info": lambda self: print("Transport info."),
#     "__str__": lambda self: f"Transport object with {id(self)}"
# })


# Car = type("Car", (Transport,), {
#     "color": lambda self: print("Car color is red")
# })


# car = Car()
# car.color()
# print(car.transport_type)
# print(car.__dict__)


# class User:

#     def __init__(self, name):
#         self.name = name


# obj = User("Fazliddin")
# print(obj.name) # Fazliddin


# class Demo:

#     def __new__(cls, *args, **kwargs):
#         print("__new__ called.")
#         instance = super().__new__(cls)
#         return instance
    
#     def __init__(self):
#         print("__init__ called.")


# demo = Demo()



# class Person:
#     _instance = None
#     _initialized = False
    
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is not None:
#             print(f"Returning instance of {cls.__name__}")
#             return cls._instance

#         print(f"Creating instance of {cls.__name__}")
#         instance = super().__new__(cls)
#         cls._instance = instance
#         return instance


#     def __init__(self, name, age):
#         if not self._initialized:
#             self.name = name
#             self.age = age
#             Person._initialized = True
#             print(f"Initializing instance of {self.__class__.__name__} with name: {self.name}, age: {self.age}")


# person = Person("Fazliddin", 21)
# print(person.name)
# person1 = Person("Asadbek", 22)
# print(person.name)


#############################################################################


#### Inheritance, mro and super() ####


# class Animal:

#     def speak(self):
#         print("Animal sound")


# class Dog(Animal):

#     def bark(self):
#         print("Woof woof")


# dog = Dog()
# dog.speak() # Animal sound
# dog.bark()  # Woof woof


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     def show(self):
#         print("D")

# obj = D()
# obj.show() # D

# print(D.mro())



# class Person:

#     def __init__(self, name):
#         self.name = name


# class Talaba(Person):
#     def __init__(self, name, university):
#         super().__init__(name)
#         self.university = university


# talaba = Talaba("Fazliddin", "TATU")
# print(talaba.name)
# print(talaba.university)


# class A:
#     def great(self):
#         print(f"Hello from A")


# class B(A):
#     def great(self):
#         super().great()
#         print(f"Hello from B")


# class C(A):
#     def great(self):
#         super().great()
#         print("Hello from C")


# class D(B, C):
#     def great(self):
#         super().great()
#         print("Hello from D")


# d = D()
# d.great()
# print(D.mro())


######################################################


#### @dataclass and __slots__ ####

# from dataclasses import dataclass

# @dataclass(frozen=False)
# class Book:
#     title: str
#     author: str
#     desc: str
#     year: int

#     def great(self):
#         print("Assalomu alaykum")


# book1 = Book("Oq kema", "Fazliddin1", "Bu juda yaxshi kitob.", 2003)
# book2 = Book("Oq kema", "Fazliddin", "Bu juda yaxshi kitob.", 2003)
# print(book1 == book2)
# book1.great()
# book1.author = "Ramziddin"
# print(book1.author)
# print(Book.__dict__)



# class Person:

#     available_attributes = ["name"]

#     __slots__ = ("name", "age")

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

#     def __repr__(self):
#         return f"Person(name={self.name}, age={self.age})"

#     def __eq__(self, value):

#         if isinstance(value, Person):
#             return self.name == value.name and self.age == value.age

#         return False
    
#     def __ne__(self, value):

#         if isinstance(value, Person):
#             return self.name != value.name or self.age != value.age

#         return False
    
#     def __getitem__(self, item):
#         print(item)
#         if item not in self.available_attributes:
#             raise ValueError("Key not found.")
#         return getattr(self, item)


# p1 = Person("Fazliddin", 21)
# 2 = Person("Fazliddin", 22)
# p1.city = "Toshkent" ❌ yangi attribute qo'shib bo'lmaydi
# print(p1.__dict__) ❌
# print(p1.name)
# print(p1==p2) # False
# print(p1['age'])





