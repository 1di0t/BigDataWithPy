#beverage =
beverage = ['Espresso', 'Compagina', 'Lemonade']
prices = [2000, 2500, 3900]
total_Price = 0
quantity = [0, 0, 0]


def select_menu(menu_number):
    """
    Print selected menu and increase quantity, totalPrice
    :param menu_number:
    :return: none
    """
    global total_Price
    print(f"{beverage[menu_number]} 주문완료")
    quantity[menu_number] += 1
    total_Price += prices[menu_number]
def print_recipe():
    print(f"움료\t가격\t수량\t{'소계':>6}\n")
    for i in range(len(beverage)):
        if quantity[i] != 0:
            print(f"{beverage[i]}\t{prices[i]}\t{quantity[i]}\t{prices[i] * quantity[i]:>6}\n")
    print(f"최종 금액 {total_Price}")


while True:
    for i in range(len(beverage)):
        print(f"{i + 1}) {beverage[i]:<15}  {prices[i]:>6}")
    try:
        menu_num = int(input(f"{len(beverage) + 1}) exit\n메뉴를 입력하세요 : "))
    except:
        print("숫자를 입력해주세요")
        continue
    
    if 0 < menu_num > (len(beverage)+2):
        print(f"{menu_num}은 존재하지 않는 메뉴입니다")
    elif menu_num == len(beverage) + 1:
        print("주문확정")
        break
    else:
        select_menu(menu_num-1)

print_recipe()

