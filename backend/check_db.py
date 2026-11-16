import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

password = os.environ.get("POSTGRES_PASSWORD")
if not password:
    raise RuntimeError("프로젝트 .env에 POSTGRES_PASSWORD를 설정해 주세요.")

with psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="room_reservation",
    user="room_app",
    password=password,
    connect_timeout=5,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result != (1,):
            raise RuntimeError("예상한 DB 응답이 아닙니다.")
        print("DB 연결 성공: SELECT 1 =", result[0])