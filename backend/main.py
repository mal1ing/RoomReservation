from fastapi import FastAPI

app = FastAPI(title="RoomReservation API")

@app.get("/health")
def health_check():
    return {"status": "ok"}