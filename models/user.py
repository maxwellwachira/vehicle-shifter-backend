from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
   name: str
   email: EmailStr
   mobile: str
   password: str
   account_type: Optional[str]
   verified_account: Optional[bool]
   disabled: Optional[bool]

   class Config:
      schema_extra = {
         "example": {
               "name": "Dickson Kahura",
               "email": "dickson69@gmail.com",
               "mobile": "0769420420",
               "password": "ComPlexPasSwORd"
         }
      }



