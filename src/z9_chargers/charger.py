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

    def create_charging_session(self, car_vin: str, charger_id: UUID, client_id: UUID) -> ChargingSession:
        csid = uuid4()
        car = self.cars.get(car_vin)
        if car is None:
            raise ValueError(f"Car with VIN {car_vin} not found.")

        charger = self.chargers.get(charger_id)
        if charger is None:
            raise ValueError(f"Charger with ID {charger_id} not found.")

        new_charging_session = ChargingSession(
            csid=csid,
            car_vin=car_vin,
            charger_id=charger_id,
            client=client_id,
            status=Charger.status,
            current_kw=Charger.max_current_kw,
            total_kwh=0.0,
            payment=0.0
        )
        # brak podanych informacji o pobieraniu opłaty i energii
        return new_charging_session



