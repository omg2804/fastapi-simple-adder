from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AdditionRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
async def add(request: AdditionRequest):
    return {"result": request.a + request.b}