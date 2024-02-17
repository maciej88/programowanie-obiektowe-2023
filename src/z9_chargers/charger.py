from argon2 import PasswordHasher

from models import *
from uuid import uuid4


class ChargingSystem:

    def __init__(self):
        self.chargers: dict[Charger] = dict()
        self.__accounts: dict[ClientAccount] = dict()
        self.cars: dict[Car] = dict()
        self.password_hasher = PasswordHasher()

    def create_account(self, name: str, funds: float, password: str):
        hashed_password = self.password_hasher.hash(password)
        new_account = {
            "id": uuid4(),
            "name": name,
            "funds": funds,
            "password": hashed_password
        }
        self.__accounts[new_account["id"]] = new_account
        return new_account

    def crete_cars(self, vin: str, max_charging_power: str) -> list[Car]:
        pass




