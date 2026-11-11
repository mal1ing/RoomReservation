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