from fastapi import FastAPI
from weather import getWeather

app = FastAPI()

@app.get("/")
def index():
    return {"message": "hello!"}

@app.get("/weather-{city}")
def weather(city):
    return getWeather(city)
