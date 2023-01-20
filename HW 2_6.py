number_goods = int(input("Введите количество товаров для базы"))

n = 0
user_list_name = []
user_list_price = []
user_list_quantity = []
user_list_measure = []

while number_goods > n:
    user_input = input("Введите название элемента")
    lenui = len(user_input)
    if lenui == 0:
        print(f"Укажите корректное название для элемента {n + 1}")
    else:
        user_list_name.append(user_input)
        n = n + 1

b = 0
while number_goods > b:
    print(f"Введите цену для элемента {user_list_name[b]}")
    user_input_price = float(input(">>>"))
    if user_input_price > 0:
        user_list_price.append(user_input_price)
        b = b + 1
    else:
        print("Укажите верную цену")

c = 0
while number_goods > c:
    print(f"Введите количество для элемента {user_list_name[c]}")
    user_input_quantity: int = int(input(">>>"))
    if user_input_quantity > 0:
        user_list_quantity.append(user_input_quantity)
        c = c + 1
    else:
        print("Укажите верное количество")

d = 0
while number_goods > d:
    print(f"Введите единицу измерения для элемента {user_list_name[d]}")
    user_input_measure = str(input(">>>"))
    lenui1 = len(user_input_measure)
    if lenui1 == 0:
        print(f"Укажите корректную единицу измерения для элемента {d + 1}")
    else:
        user_list_measure.append(user_input_measure)
        d = d + 1

e = 0
t: int = 0
list1_1_2 = ("name", "price", "quantity", "measure")
g: list[int] = [i for i in range(0, number_goods)]
k: list[int] = [r for r in range(0, number_goods)]

while number_goods > e:
    values = (user_list_name[e], user_list_price[e], user_list_quantity[e], user_list_measure[e])
    g[e] = dict(zip(list1_1_2, values))
    print(f"dict {e+1} :{g[e]}")
    e = e + 1

list_name = []
list_price = []
list_measure = []
list_quantity = []

while number_goods > t:
    list_name.append(g[t].get('name'))
    list_price.append(g[t].get('price'))
    list_measure.append(g[t].get('measure'))
    list_quantity.append(g[t].get('quantity'))
    t = t + 1

print("Results:")
print(f"Наименование {list_name}")
print(f"Цена {list_price}")
print(f"Количество {list_quantity}")
print(f"Мера {list_measure}")
