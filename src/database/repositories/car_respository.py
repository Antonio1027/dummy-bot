import json

class CarRepository():

    @staticmethod
    def get_cars():
        file = open('./src/database/cars.json')
        data = json.load(file)
        return data.get("Cars", {})

    @staticmethod
    def get_cars_by_brand(brand: str) -> dict:
        data = CarRepository.get_cars()
        return list(filter(lambda car: car.get("make", "") == brand, data))
    

    @staticmethod
    def get_cars_with_detail(year: str, version: str):
        data = CarRepository.get_cars()
        return list(filter(lambda car: car.get("year", "") == year and car.get("version", "") == version, data))