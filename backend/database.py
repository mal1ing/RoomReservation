import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

def get_connection():
    password = os.environ.get("POSTGRES_PASSWORD")
    if not password:
        raise RuntimeError(
            "프로젝트 .env에 POSTGRES_PASSWORD를 설정해주세요."
        )

    return psycopg.connect(
        host="127.0.0.1",
        port=5432,
        dbname="room_reservation",
        user="room_app",
        password=password,
        connect_timeout=5,
    )