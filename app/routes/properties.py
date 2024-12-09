from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data.properties_data import property_listings
from app.models.property_models import PropertyCreate


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

# Define the route for adding a new property
@router.post("/properties")
def add_property(property: PropertyCreate):
    # Calculate the next available ID
    if property_listings:
        next_id = max(item["id"] for item in property_listings) + 1
    else:
        next_id = 1  # Start from 1 if the list is empty

    # Create the new property with the auto-incremented ID
    new_property = property.dict()
    new_property["id"] = next_id

    # Add the new property to the list
    property_listings.append(new_property)
    return {"message": "Property added successfully", "property": new_property}

    # Define the route for deleting a property by ID
@router.delete("/properties/{property_id}")
def delete_property(property_id: int):
    for property in property_listings:
        if property["id"] == property_id:
            property_listings.remove(property)  # Remove the property from the list
            return {"message": f"Property with ID {property_id} deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Property not found")