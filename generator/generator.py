from data.data import Person
from faker import Faker

"""Используем библиотеку faker для генерации рандомных данных"""
faker_ru = Faker('ru_RU')  # создаём экземпляр класса и указываем язык


def generated_person():  # генератор данных
    yield Person(  # yield возвращает иттерируемый список из которого будем получать иттераторы(элементы списка)
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_adress=faker_ru.address(),
        permanent_adress=faker_ru.address()
    )
