import re

from pydantic import validator
from pydantic.dataclasses import dataclass


regex = r"978[-0-9]{10,15}"
pattern = re.compile(regex)


@dataclass(frozen=True)
class Isbn:
    """Isbn represents an ISBN code as a value object"""

    value: str

    @validator("value")
    def validate_isbn_value(cls, v):
        if pattern.match(v) is None:
            raise ValueError("isbn should be a valid format.")

        return v
