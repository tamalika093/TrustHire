
from fastapi import FastAPI

# Import the offer analysis router
from app.routers.offer import router as offer_router
from app.routers.url import router as url_router

# Create our TrustHire application
app = FastAPI(
    title="TrustHire API",
    description="An AI-powered platform to detect fraudulent job and internship offers.",
    version="1.0.0"
)


# Register the offer analysis router
app.include_router(offer_router)
app.include_router(url_router)

# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to TrustHire Backend!",
        "status": "Running successfully"
    }


# Health check route
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "project": "TrustHire"
    }
