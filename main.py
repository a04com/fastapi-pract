from fastapi import FastAPI
from weather import getForecast
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/weather")
async def weather(q: str, days: int):
    return getForecast(q, days)
