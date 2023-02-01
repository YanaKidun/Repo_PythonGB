"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name: str,
              surname: str,
              birth_year: int,
              city: str,
              email: str,
              phone: int
              ):

    return f"{name} {surname} {birth_year} года рождения, " \
           f"в городе {city}. Контакты: {email}, {phone} "


def user_data_kw(**kwargs) -> str:

    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone} "