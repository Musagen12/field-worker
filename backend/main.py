from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.database import create_db_and_tables
from contextlib import asynccontextmanager
from routes import complaints, auth, worker, admin,sms
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="Field Service Tracker", lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:8080", "http://localhost:8080"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path where images are stored
UPLOAD_DIR = "uploads"

# Make sure the folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Expose uploads directory at /uploads
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")
app.include_router(auth.router, prefix="/auth")
app.include_router(admin.router, prefix="/admin")
app.include_router(worker.router, prefix="/worker")
app.include_router(complaints.router, prefix="/complaints")
app.include_router(sms.router, prefix="/sms")

@app.get("/", tags=["Test"])
def root():
    return {"message": "Field Service Tracker API running"}
