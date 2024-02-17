from argon2 import PasswordHasher

from models import *
from uuid import uuid4


class ChargingSystem:

    def __init__(self):
        self.chargers = list()
        self.__accounts = list()
        self.cars = {}
        self.password_hasher = PasswordHasher()

    def create_account(self, name: str, funds: float, password: str):
        hashed_password = self.password_hasher.hash(password)
        new_account = {
            "id": uuid4(),
            "name": name,
            "funds": funds,
            "password": hashed_password
        }
        self.__accounts.append(new_account)
        return new_account

    def crete_cars(self, vin: str) -> list[Car]:
        pass




