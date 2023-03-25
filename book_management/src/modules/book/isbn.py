#
# ISBN에 대해 정의
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/03/25 23:01 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import re


from pydantic import BaseModel, validator

regex = r"978[-0-9]{10,15}"
pattern = re.compile(regex)


class Isbn(BaseModel):
    """Isbn represents an ISBN code as a value object"""

    value: str

    @validator("value")
    def validate_isbn_value(cls, v):
        if pattern.match(v) is None:
            raise ValueError("isbn should be a valid format.")

        return v
