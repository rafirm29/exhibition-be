from pydantic import BaseModel

class Dream(BaseModel):
    name: str
    message: str