
from fastapi import FastAPI
from src.app.database.repositories.car_respository import CarRepository

app = FastAPI()

@app.get("/")
def read_root():
    return CarRepository.get_cars()

@app.get("/cars/{brand}")
def read_item(brand: str):
    return CarRepository.get_cars_by_brand(brand)
