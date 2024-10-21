from pydantic import BaseModel

class Config(BaseModel):
    uin: str = ""
    skey: str = ""