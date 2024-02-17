from argon2 import PasswordHasher

from models import *
from uuid import uuid4


class ChargingSystem:

    def __init__(self):
        self.chargers: dict[Charger] = dict()
        self.__accounts: dict[ClientAccount] = dict()
        self.cars = dict()
        self.password_hasher = PasswordHasher()

    def create_account(self, name: str, funds: float, password: str) -> ClientAccount:
        hashed_password = self.password_hasher.hash(password)
        new_account = ClientAccount(
            id=uuid4(),
            name=name,
            funds=funds,
            password=hashed_password
        )
        self.__accounts[new_account.id] = new_account
        return new_account

    def crete_cars(self, vin: str, max_charging_power: str) -> Car:
        new_car = Car(vin, 0.0, max_charging_power)
        self.cars[vin] = new_car
        return new_car

    def create_charger(self, max_current_kw: float) -> Charger:
        serial_no = uuid4()
        new_charger = Charger(serial_no, max_current_kw, 0.0, True)
        self.chargers[new_charger.serial_no] = Charger
        return new_charger







