# DDD 접근법 학습

이 리포지토리는 DDD(Domain-driven Design)을 통하여 "도서관" 프로젝트를 풀어나가는 과정을 기록한다.

# Preface

이 리포지토리를 만들고 기획하기에 앞서 아래 프로젝트들에 크게 영향을 받았다. (감사합니다!)

## 코드도출과정

1. https://github.com/pgorecki/python-ddd
    1. 이 코드는 이베이 `bidding` 을 일부 구현했고 해제까지 해놓음
    2. 3번보다 더 빡세게 코드구조가 되어있음. 종국에는 모두 참고할 것임.
2. https://github.com/slimovich/Realworld-fastapi-gino-template
    1. 유저 관련 딱 기본만 작업되어 있음
3. https://github.com/iktakahiro/dddpy
    1. 도서 관리 시스템을 기반으로 함
    2. 있을 건 있음. 패턴화해서 작업한게 되게 많다!
        1. 읽기/쓰기 모델 분리 → CQRS에 기반이 되도록...
        2. CQRS
        3. UoW
            1. 트랜잭션 관리용
        4. 팩토리
4. https://github.com/GArmane/python-fastapi-hex-todo
    1. Todo list에 대한 내용임
    2. 로그인 후 관련 처리하는 내용이 있음
    3. response 분류를 미약하게나마 해놨음
    4. 개인적으로 많이 참고했음
5. [https://github.com/fkromer/code/tree/appendix_fastapi](https://github.com/fkromer/code/tree/appendix_fastapi)
    1. DDD를 FastAPI로 해놨다. 참고하기

# 도메인 도출과정

각 프로젝트 디렉토리 별로 설명한다.

# 개발과정

## 프로젝트 추기 구성

일단 어떤 프로젝트로 갈지는 상단 3번을 따라간다. 필요하면 추가로 구현한다.

## 리포지토리 구성

최소단위를 만들고 재구성할 예정

# 코드 구성

모노레포(예정)

# 유용한 명령어들

각 프로젝트 별 README 파일을 참조한다.
