from datetime import datetime
from uuid import UUID


class ClientAccount:
    id: UUID
    name: str
    funds: float
    password: str


class Car:
    vin: str
    total_charged_kwh: float
    max_charging_power: float


class Charger:
    serial_no: UUID
    max_current_kw: float
    total_charged_kw: float
    status: bool


class ChargingSession:
    csid: UUID
    car_vin: UUID
    charger_id: UUID
    client: UUID
    status: bool
    current_kw: float
    total_kwh: float
    payment: float


class ChargingStatus:
    OPEN: bool
    ERROR: bool
    FINISHED: bool


class ChargingService:
    chargers: list[Charger]
    time_modifier: datetime  # (for testing)





# class ChargerStatus:
#     FREE: bool
#     CHARGING: bool
#     ERROR: bool
