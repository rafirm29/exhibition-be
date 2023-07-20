from pydantic import BaseModel

class FeedbackData(BaseModel):
    name: str
    feedback: str