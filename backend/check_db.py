from database import get_connection

with get_connection() as connection: 
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result != (1,):
            raise RuntimeError("예상한 DB 응답이 아닙니다.")
        print("DB 연결 성공: SELECT 1=", result[0])