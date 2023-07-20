from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    feedback: str