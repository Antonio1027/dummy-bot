import json

class CarRepository():

    @staticmethod
    def get_cars():
        file = open('./src/app/database/data.json')
        data = json.load(file)
        return data.get("Cars", {})

    @staticmethod
    def get_cars_by_brand(brand: str):
        data = CarRepository.get_cars()
        return list(filter(lambda car: car.get("make", "").lower() == brand, data))