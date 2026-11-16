import psycopg
from fastapi import FastAPI, HTTPException

from database import get_connection

app = FastAPI(title="RoomReservation API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def database_health_check(): 
    try:
        with get_connection() as connection: 
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

        if result != (1,):
            raise HTTPException(
                status_code=503,
                detail="DB 상태를 확인할 수 없습니다.",
            )
 
    except(psycopg.Error, RuntimeError):
        raise HTTPException(
            status_code=503,
            detail="DB 상태를 확인할 수 없습니다.",
        ) from None

    return {"status": "ok", "database": "ok"}