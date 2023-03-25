# 도서 관리 프로젝트

이 프로젝트에서는 도서를 관리하는 시스템에 대해 논의한다.

## 쉽게 입문해봅시다

사서의 관점에서...

도서에 대해 무엇을 할 수 있나?

- 조회가능 (개발도서 검색)
- 개별도서조회 가능 (별도 도서의 id로 검색)
- 도서정보 추가(등록) 가능
- 도서정보 수정 가능
- 도서정보 삭제 가능

## 프로젝트 구조

```
.
├── src
│   ├── api
│   ├── config
│   ├── modules
│   │   └── book
│   └── utils
└── tests
    ├── modules
    │   └── book
    └── utils
```

## 개발 시 필요한 사항

### 설치 필요

- Python 3.10 이상
- [Docker](https://www.docker.com/get-started) 설치

### 라이브러리 및 추가 설정

- `poetry`를 통한 라이브러리 설치
  - `poetry install`
- `pre-commit` 훅 설치 및 테스트
  - `pre-commit install`
  - `pre-commit run`

## 서버 구동

다음과 같이 make 커맨드를 실행한다.

```bash
make up
```

## 유용한 명령어들

```shell
make test             # 전체 테스트코드 구동
make build            # 도커 이미지 업데이트 시 사용
make ps               # 도커 컨테이너 구동상태 확인
make shell-redis      # (구동중일 때) Redis 컨테이너의 redis-cli에 접속
make shell-postgres   # (구동중일 때) PostgreSQL 컨테이너의 shell에 접속
make down             # 구동중인 모든 컨테이너 종료
```
