# 개발 환경 실행

## 기준 환경

- Windows CMD
- Python 3.13.1
- 명령어는 프로젝트 최상위 폴더에서 실행한다.

## 가상환경 생성

```cmd
py -3.13 -m venv backend\.venv
```

## 패키지 설치

```cmd
backend\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt
```

## 개발 서버 실행

```cmd
backend\.venv\Scripts\python.exe -m uvicorn main:app --app-dir backend --reload
```

## 동작 확인

- http://127.0.0.1:8000/health
  - HTTP 200, {"status":"ok"} 응답 확인
- http://127.0.0.1:8000/docs
  - Swagger UI에서 GET /health 실행 가능

현재 health API는 서버 응답만 확인하며 DB 연결은 검사하지 않는다.

## 서버 종료

실행 중인 터미널에서 Ctrl + C를 누른다.

## PostgreSQL 실행

Docker Desktop을 먼저 실행한다.
명령은 프로젝트 최상위 폴더의 Windows CMD에서 실행한다.

### 로컬 설정

.env.example을 .env로 복사하고 POSTGRES_PASSWORD 값을 설정한다.
.env에는 개발용 비밀번호를 작성하며 Git에 올리지 않는다.

이미 .env가 있다면 덮어쓰지 않는다.

### 설정 검증 및 실행

```cmd
docker compose config --quiet
docker compose up -d db
docker compose ps
```

db 서비스가 healthy 상태인지 확인한다.

### Python에서 DB 연결 확인

```cmd
backend\.venv\Scripts\python.exe backend\check_db.py
```

예상 결과: DB 연결 성공: SELECT 1 = 1

이 스크립트는 DB 접속을 확인한다.
FastAPI의 /health는 아직 DB 연결을 검사하지 않는다.

### DB 중지 및 재시작

```cmd
docker compose stop db
docker compose start db
```

중지해도 데이터는 Docker 볼륨에 유지된다.
POSTGRES_PASSWORD는 최초 DB 초기화에 사용된다.
이후 .env 값만 바꿔도 기존 DB의 비밀번호가 변경되지는 않는다.