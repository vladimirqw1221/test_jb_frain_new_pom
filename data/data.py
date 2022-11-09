from dataclasses import dataclass


@dataclass
class Person:
    fist_name: str = None
    last_name: str = None
    zip_code: str = None
