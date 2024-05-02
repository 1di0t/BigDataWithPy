# beverage = ['Espresso', 'Compagina', 'Lemonade']
# prices = [2000, 2500, 3900]

beverage_Price = {'Espresso':2000,'Compagina':2500,'Lemonade':3900}
total_Price = 0
quantity = [0, 0, 0]


def print_menu():
    i = 0
    for menu, price in beverage_Price.items():
        print(f"{i + 1}) {menu:<15}  {price:>6}")
        i= i+1
    print(f"{len(beverage_Price)+1}) exit")

while True:
    print_menu()
    try:
        menu_num = int(input("메뉴를 입력하세요 : "))
    except:
        print("숫자를 입력해주세요")
        continue

