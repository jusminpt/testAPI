from fastapi import FastAPI
from app.routes.properties import router as properties_router  # Import your router

app = FastAPI()

# Include the router in the main app
app.include_router(properties_router, prefix="/api", tags=["Properties"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the property API!"}
