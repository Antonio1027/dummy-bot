from src.services.messages.api import get_response
from src.database.repositories.car_respository import CarRepository
from src.database.repositories.brand_repository import BrandRepository
from src.services.openia.api import get_completion_from_messages

def message_processor(query: str, user_number: str, sender_number: str):
    brands_list = BrandRepository.get_brands()
    brands = "\n".join(brands_list)
    cars_with_details = ""
    cars_by_brand = ""
    for brand in brands_list:
        cars_by_brand += f"{brand}: \n"
        cars = CarRepository.get_cars_by_brand(brand)
        for car in cars:
            cars_by_brand += f"Modelo: {car.get('model')} {car.get('year')}\nVersión: {car.get('version')} \n\n"
            cars_with_details += get_cars_with_detail(car)

    system_content = f"""
        You are a commercial agent at Kavak, just respond in spanish.
        You can get and summarize information from this website https://www.kavak.com/mx/blog/sedes-de-kavak-en-mexico
        to make known the company's value proposition.

        List of brands of available cars in the catalog:
        {brands}

        List of availabe cars by brand:
        {cars_by_brand}

        List of cars with detail information:
        {cars_with_details}

        You can offer financing plans based on the down payment, the price of the car, a 10% interest rate, and financing terms between 3 and 6 years.
        Calculate the financing plan if the cliente request the plan
    """
    messages = [
        {"role": "system", "content": system_content},
        {
            "role": "user",
            "content": query,
        },
    ]
    content = get_completion_from_messages(messages)
    get_response(content, user_number, sender_number)
    return {
        "message": str(content)
    }


def get_cars_with_detail(car: dict):
    content = "**Información del auto:** \n"
    content += f"""
        Marca: {car.get('make')}\n
        Modelo: {car.get('model')}\n
        Año: {car.get('year')}\n
        Versión: {car.get('version')}\n
        Precio: {car.get('price')}\n
        Kilometraje: {car.get('km')}\n
        Bluetooth: {car.get('bluetooth')}\n\n
        **Medidas**\n
        Largo: {car.get('largo')}\n
        Ancho: {car.get('Ancho')}\n
    \n"""
    return content