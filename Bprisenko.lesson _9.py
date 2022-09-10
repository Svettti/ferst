
# Клиент (то есть вы) приходит в кондитерскую. Он хочет приобрести один или несколько видов продукции,
# а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
#
# Предложите выбор:
# 1.  Если человек хочет посмотреть описание: название – описание
# 2.  Если человек хочет посмотреть цену: название – цена.
# 3.  Если человек хочет посмотреть количество: название – количество.
# 4.  Всю информацию.
# 5.  Приступить к покупке:
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке
# 6.  Сказать: «До свидания!»

menu={
       "bun":[["мука","сахар","яйца","сливки"], 3.75, 2500],
        "cake":[["состав"], 2.5, 250],
        "ice cream":[["состав1"], 4, 400],
      }
menu1 = " "
#while True:  # вся информация
menu1=input('Print all menu? (yes\ no) - ')
if menu1=="yes":
    for key, value in menu.items():
        print(f'{key} - {value[0]} - {value[1]} - {value[2]} ')
    else: print()
compound = " "
while True:           # информация по каждому товару
        menu1= input('Введите  название продукта,  если закончить -"end" :   ' )
        if menu1 == "end" or menu1 not in menu.keys(): break
        compound = input("Введите что хотите узнать: comp, price, weight? -")
        if compound == "comp": print(menu1,menu[menu1][0])
        elif compound == "price": print(menu1,menu[menu1][1])
        elif compound == "weight": print(menu1,menu[menu1][2])
        if menu1 == "end" or menu1 not in menu.keys(): break

buy = ''     # продажа
price = 0
while True:
    buy = input('Что вы хотите купить? (n - выход) ')
    if buy == 'n' or buy not in menu.keys(): break
    kol = int(input('Сколько: '))
    if kol > menu[buy][2]:
        print('Столько товаров нет!')
        continue
    price += (kol * menu[buy][1])/100
    menu[buy][2] -= kol
print('Итоговая цена: ', price)
print("До свидания")
for key, value in menu.items():
    print(f'{key} - {value[0]} - {value[1]} - {value[2]} ')