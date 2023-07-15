from pydantic import BaseModel

class VisitorData(BaseModel):
    title: str
    name: str
    origin: str
    exhibition_info_source: str