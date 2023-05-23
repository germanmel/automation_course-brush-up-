from data.data import Person
from faker import Faker
from random import randint

"""Используем библиотеку faker для генерации рандомных данных"""
faker_ru = Faker('ru_RU')  # создаём экземпляр класса и указываем язык


def generated_person():  # генератор данных
    yield Person(  # yield возвращает иттерируемый список из которого будем получать иттераторы(элементы списка)
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=randint(10, 80),
        department=faker_ru.job(),
        salary=randint(15000, 150000),
        email=faker_ru.email(),
        current_adress=faker_ru.address(),
        permanent_adress=faker_ru.address()
    )

def generated_file():
    path = rf'D:\_QA_study\automation_course_brush_up\testfile{randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f"Test text{randint(0,999)}")
    file.close()
    return file.name, path
