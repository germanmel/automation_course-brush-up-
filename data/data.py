from dataclasses import dataclass

"""В data указываем какие данные нужны для генерации"""

"""Класс python для генерации данных, не нужно делать init и назначать self переменные, формат как по коду ниже,
тип данных обязателен, иначе строка будет игнорироваться"""
@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_adress: str = None
    permanent_adress: str = None
    mobile: str = None
    birthday: int = None

@dataclass()
class Color:
    color_name: list = None