from dataclasses import dataclass
from abc import ABC, abstractmethod

# User ma'lumotlar bazasi
USERS_DB = [
    {
        "name": "Fazliddin",
        "phone_number": "+998907205768",
        "password": "1234",
        "balance": 100_000_000
    },
    {
        "name": "Ramziddin",
        "phone_number": "+999892345678",
        "password": "1234",
        "balance": 200_000_000
    }
]


# Foydalanuvchi modeli

@dataclass(frozen=True)
class User:
    name: str
    phone_number: str
    password: str
    balance: int


# Abstract class (strategiya interfeysi)

class ATMOperation(ABC):
    @abstractmethod
    def execute(self, user: User):
        pass


# Strategy pattern (Operatsiyalar)

class BalanceCheck(ATMOperation):

    def execute(self, user: User):
        print(f"Sizning balansingiz: {user.balance}")


class Withdraw(ATMOperation):

    def execute(self, user: User):
        amount = int(input("Yechmoqchi bo'lgan summangizni kiriting: "))
        if amount <= user.balance:
            user.balance -= amount
            print(f"{amount} so'm yechildi. Qolgan {user.balance} so'm")
        else:
            print(f"Mablag' yetarli emas.")


class Deposit(ATMOperation):

    def execute(self, user: User):
        amount = int(input("Qo'shmoqchi bo'lgan so'mmani kiriting: "))











