from pydantic import BaseModel

class DreamData(BaseModel):
    name: str
    message: str