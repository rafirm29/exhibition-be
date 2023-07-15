from pydantic import BaseModel

class Visitor(BaseModel):
    title: str
    name: str
    origin: str
    exhibition_info_source: str