from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

class Item(BaseModel):
    name: str
    husband: str
    age: int
    weight: int

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["StudyStack"]
collection = db["vidhi"]

@app.post("/items")
async def create_item(item: Item):
    await collection.insert_one(item.model_dump())
    return "success"

