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

- Python 3.8 이상
  - (if possible) pyenv 를 통한 개별 환경을 구성할 것을 추천!
    - [Simple Python Version Management: pyenv](https://github.com/pyenv/pyenv) 
    - [poetry: Managing environments](https://python-poetry.org/docs/managing-environments/)
- 운영체제 환경에 맞는 [Docker](https://www.docker.com/get-started) 설치

### 라이브러리 및 추가 설정

- `poetry`를 통한 라이브러리 설치
  - `poetry install`
- `pre-commit` 훅 설치 및 테스트
  - `pre-commit install`
  - `pre-commit run`

## 서버 구동 (개발환경)

다음과 같이 make 커맨드를 실행합니다.

```bash
make dev-up
```

구동을 종료하기 위해선 아래 명령을 입력합니다.

```bash
make dev-down
```

## 서버 구동 (프로덕션 환경)

다음과 같이 make 커맨드를 실행합니다.

```bash
make prod-up
```

구동을 종료하기 위해선 아래 명령을 입력합니다.

```bash
make prod-down
```

## Swagger API 정보

Swagger API 및 OAS 3.0 스펙문서 제공 경로는 아래와 같습니다.

- Swagger 페이지 `http://localhost:8000/docs`
- ReDoc 페이지 `http://localhost:8000/redoc`
- OAS 3.0 스펙 다운로드 경로 `http://localhost:8000/openapi.json`

## 유용한 명령어들

### 테스트

```shell
make test                # 전체 테스트코드 구동
make cov                 # 테스트 커버리지 확인 - stdout으로 결과 확인
make cov-html            # 테스트 커버리지 확인 - 웹 브라우저로 결과 확인 (book_management/htmlcov/index.html 파일로 결과 확인)
```

### 개발환경 커맨드

```shell
make build-dev           # 도커 이미지 업데이트 시 사용
make dev-ps              # 도커 컨테이너 구동상태 확인
make dev-shell-redis     # (구동중일 때) Redis 컨테이너의 redis-cli에 접속
make dev-shell-postgres  # (구동중일 때) PostgreSQL 컨테이너의 shell에 접속
```

### 운영환경 커맨드

```shell
make build-prod          # 도커 이미지 업데이트 시 사용
make prod-ps             # 도커 컨테이너 구동상태 확인
make prod-shell-redis    # (구동중일 때) Redis 컨테이너의 redis-cli에 접속
make prod-shell-postgres # (구동중일 때) PostgreSQL 컨테이너의 shell에 접속
```

## Workarounds

### (개발환경) 도커 이미지 디버깅

프로세스가 어떤식으로 떠있는지 확인하기 위해, 도커 컨테이너에 접근 후 아래 명령을 수행하여 `ps` 명령을 수행합니다.

```shell
apt-get update && apt-get install procps
```
