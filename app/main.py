from fastapi import FastAPI
from app.routers import applications

app = FastAPI(title="AppTrack Job Application Tracker")

app.include_router(applications.router)

@app.get("/health", status_code=200)
def health_check():
    return {"status": "ok"}