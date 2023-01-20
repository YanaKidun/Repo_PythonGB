# задание 5 Прибыль и рентабельность организации
revenue = int(input("Введите выручку >>>"))
costs = int(input("Введите издержки >>>"))
if revenue > costs:
    print("Ваша организация работает с прибылью")
elif revenue == costs:
    print("Ваша организация работает без прибыли")
else:
    print("Ваша организация работает в убыток")

if revenue > costs:
    employees = int(input("Введите количество сотрудников >>>"))
    rent = round(float(revenue / costs), 2)
    procrent = round(rent * 100, 2)
    rentemployees = round(float(revenue / employees), 2)
    print(
        "Коэффициент рентабельности Вашей организации равен {} или {} процентов, "
        "а прибыль на одного сотрудника равна {}".format(rent, procrent, rentemployees))
else:
    print("Ваша организация работает в убыток или без прибыли")

