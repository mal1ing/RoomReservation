# API 설계

## 방 목록 조회

### 요청

GET /api/rooms?date=2026-11-20&attendees=4

인증: 불필요

| 파라미터 | 의미 | 필수 |
|---|---|---|
| date | 이용 날짜, YYYY-MM-DD | 필수 |
| attendees | 이용 인원, 양의 정수 | 필수 |

### 응답 예시

HTTP 200 OK

```json
{
  "items": [
    {
      "id": 1,
      "name": "A룸",
      "description": "화이트보드와 모니터가 있는 공간",
      "capacity": 6,
      "hourly_rate": 10000,
      "currency": "KRW"
    }
  ]
}
```

### 조회 규칙

- 선택한 이용일에 적용되는 정책으로 정원과 요금을 조회한다.
- 정원이 요청 인원 이상인 방을 반환한다.
- 조건에 맞는 방이 없으면 HTTP 200과 빈 items 배열을 반환한다.
- 시간을 지정하지 않았으므로 특정 시간의 예약 가능 여부는 보장하지 않는다.

### 입력 검증

- date는 YYYY-MM-DD 형식의 유효한 날짜여야 한다.
- 과거 날짜는 한국 날짜 기준으로 조회할 수 없다.
- attendees는 1 이상의 정수여야 한다.
- 필수 파라미터가 누락되면 입력 오류를 반환한다.

### 입력 오류 응답 예시

요청: GET /api/rooms?date=2026-11-20&attendees=0

HTTP 422 Unprocessable Content

```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": ["query", "attendees"],
      "msg": "Input should be greater than or equal to 1",
      "input": "0",
      "ctx": {
        "ge": 1
      }
    }
  ]
}
```

오류 메시지의 세부 표현은 FastAPI·Pydantic 버전에 따라 달라질 수 있다.
프론트엔드는 msg 문자열을 직접 비교하지 않고 loc와 type을 기준으로 안내한다.

## 방 상세 조회

### 요청

GET /api/rooms/1?date=2026-11-20

인증: 불필요

| 파라미터 | 위치 | 의미 |
|---|---|---|
| room_id | 경로 | 조회할 방 ID, 양의 정수 |
| date | 쿼리 | 이용 날짜, YYYY-MM-DD |

### 정상 응답 예시

HTTP 200 OK

```json
{
  "id": 1,
  "name": "A룸",
  "description": "화이트보드와 모니터가 있는 공간",
  "policy": {
    "id": 101,
    "effective_from": "2026-11-01",
    "capacity": 6,
    "hourly_rate": 10000,
    "currency": "KRW",
    "cancellation_notice_minutes": 1440
  }
}
```

### 오류

- 방이 존재하지 않으면 HTTP 404를 반환한다.
- room_id나 date의 형식이 잘못되면 HTTP 422를 반환한다.
- 선택일에 적용할 정책이 없는 경우의 처리는 추후 결정한다.

운영시간·예약 단위·공지 응답은 정책 설계 보완 후 추가한다.

경로: GET /api/rooms/{room_id}
예시: GET /api/rooms/1?date=2026-11-20