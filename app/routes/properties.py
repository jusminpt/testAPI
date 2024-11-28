from fastapi import APIRouter
from app.data.properties_data import property_listings

# Create a router instance
router = APIRouter()

# Define the route for retrieving all properties
@router.get("/properties")
def get_properties():
    return property_listings

# Define the route for retrieving a property by ID
@router.get("/properties/{property_id}")
def get_property_by_id(property_id: int):
    for property in property_listings:
        if property["id"] == property_id:
            return property
    return {"error": "Property not found"}
