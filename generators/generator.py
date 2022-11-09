from data.data import Person
from faker import Faker
facer_ru = Faker("ru_RU")


def generated_person():
    yield Person(fist_name= facer_ru.first_name(),
                 last_name=facer_ru.last_name(),
                 zip_code= facer_ru.postcode()
                 )