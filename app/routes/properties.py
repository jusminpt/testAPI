from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data.properties_data import property_listings

# Create a router instance
router = APIRouter()

# Define a Pydantic model for the request body
class PropertyUpdate(BaseModel):
    description: str

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
    raise HTTPException(status_code=404, detail="Property not found")

# Define the route for updating the description of a property by ID
@router.patch("/properties/{property_id}")
def update_property_description(property_id: int, property_update: PropertyUpdate):
    for property in property_listings:
        if property["id"] == property_id:
            property["description"] = property_update.description  # Update the description
            return {"message": "Description updated successfully", "property": property}
    
    raise HTTPException(status_code=404, detail="Property not found")