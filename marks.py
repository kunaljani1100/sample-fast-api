from contextlib import nullcontext
from operator import is_not
from symbol import return_stmt

from fastapi import FastAPI
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

MONGO_URI = "mongodb://host.docker.internal:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["StudyStack"]
collection = db["vidhi"]

class Student(BaseModel):
    firstname: str
    lastname: str
    physics: int = Field(..., gt=0, lt=100)
    chem: int = Field(..., gt=0, lt=100)
    maths: int = Field(..., gt=0, lt=100)


@app.get("/")
async def read_root():
    cursor = collection.find({"physics": {"$gt": 90}})

    result = []

    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        result.append(doc)

    return result


@app.post("/items/")
async def create_item(item: Student):
    await collection.insert_one(item.model_dump())
    return "success"

@app.get("/health")
async def health():
    return "app is healthy"


