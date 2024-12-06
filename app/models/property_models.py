from pydantic import BaseModel

class PropertyCreate(BaseModel):
    location: str
    size_sqm: int
    amenities: list[str]
    price: int
    type: str
    description: str = ""
