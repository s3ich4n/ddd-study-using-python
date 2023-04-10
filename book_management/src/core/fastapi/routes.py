#
# 라우터 추가 관련 헬퍼 함수
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/079 15:22 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from fastapi import FastAPI


def add_routes(routes, app: FastAPI):
    for route in routes:
        app.include_router(route)
