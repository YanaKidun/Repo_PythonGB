# Задание 3. Сообщить к какому времени года относится месяц

month1 = int(input("Введите номер месяца:"))
season_dict = {"1": "winter", "2": "spring", "3": "summer", "4": "autumn"}
season_list = ["winter", "spring", "summer", "autumn"]

if month1 < 1 or month1 > 12:
    print("Input correct number")

elif month1 == 12 or month1 == 1 or month1 == 2:
    print(season_dict.get("1"))
    print(f"Hi, it's {season_list[0]}!")

elif 2 < month1 <= 5:
    print(season_dict.get("2"))
    print(f"Hi, it's {season_list[1]}!")

elif 5 < month1 <= 8:
    print(season_dict.get("3"))
    print(f"Hi, it's {season_list[2]}!")

elif 8 < month1 <= 11:
    print(season_dict.get("4"))
    print(f"Hi, it's {season_list[3]}!")
