import datetime

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Locations ------------------------------------
class LocationsBase(BaseModel):
    id: int
    name: str
    org_id: int
    latitude: float
    longitude: float
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CreateLocation(LocationsBase):
    class Config:
        orm_mode = True


