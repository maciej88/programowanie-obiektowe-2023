from uuid import UUID


class ClientAccount:
    id: UUID
    name: str
    funds: float


class Car:
    vin: str
    total_charged_kwh: float
    max_current_kw: float


class ChargingSession:
    csid: UUID
    status: bool
    current_kw: float
    total_kwh: float


class ChargingStatus:
    OPEN: bool
    ERROR: bool
    FINISHED: bool


class ChargingService:
    chargers: list[Charger]
    time_modifier: float  # (for testing)


class Charger:
    max_current_kw: float
    total_charged_kw: float
    attached_car_vin: str
    status: bool


class ChargerStatus:
    FREE: bool
    CHARGING: bool
    ERROR: bool
