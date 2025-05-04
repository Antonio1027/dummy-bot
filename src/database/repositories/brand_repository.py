import json

class BrandRepository():

    @staticmethod
    def get_brands():
        file = open('./src/database/brands.json')
        data = json.load(file)
        return data.get("Brands", {})