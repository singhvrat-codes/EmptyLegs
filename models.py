from pydantic import BaseModel
from typing import Optional

class DriverRoute(BaseModel):
    driver_name: str
    origin_lat: float
    origin_lng: float
    dest_lat: float
    dest_lng: float
    capacity_kg: Optional[float] = 0

class Shipment(BaseModel):
    shipper_name: str
    pickup_lat: float
    pickup_lng: float
    drop_lat: float
    drop_lng: float
    weight_kg: float

class Match(BaseModel):
    id: int
    driver_name: str
    score: float
    price: float
    co2_saved: float
