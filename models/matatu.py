import imp
from typing import Optional
from pydantic import BaseModel

class Matatu(BaseModel):
    reg: str
    stage: str
    to: str
    fare: int
    driver: str
    date: Optional[str]
    time: Optional[str]
    status: Optional[str]
    done_date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "reg": "KBJ 069A",
                "stage": "Nairobi",
                "to": "Nyeri",
                "fare": "450",
                "driver": "Dickson"
            }
        }

class Date(BaseModel):
    date: str
    time: str

