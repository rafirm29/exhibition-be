from fastapi import FastAPI, HTTPException
from typing import List

from db.database import collection_visitor, collection_dream
from schemas.visitor import VisitorData
from schemas.dream import DreamData

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is up and running"}

@app.post("/form", response_model=VisitorData)
async def submit_form(payload: VisitorData):
    if any(value is None or value == "" for value in payload.dict().values()):
        raise HTTPException(400, "Invalid payload. All fields must be filled.")
    
    await collection_visitor.insert_one(dict(payload))
    return payload

@app.post("/dream", response_model=DreamData)
async def submit_dream(payload: DreamData):
    if any(value is None or value == "" for value in payload.dict().values()):
        raise HTTPException(400, "Invalid payload. All fields must be filled.")
    await collection_dream.insert_one(dict(payload))
    
    return payload


@app.get("/dream", response_model=List[DreamData])
async def get_dreams():
    response = await collection_dream.find().to_list(1000)
    
    return response