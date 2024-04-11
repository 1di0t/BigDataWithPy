beverage = ['Espresso','Compagina']
prices = [2000,2500]
total_Price = 0

while True:
    menu_num = int(input(f" {0}) {beverage[0]} : {prices[0]} \n {1}) {beverage[1]} : {prices[1]} \n {len(beverage)+1}) exit\n 메뉴를 입력하세요 :"))
    if menu_num == 3:
        print("주문확정")
        break
    elif menu_num == 1:
        print(f"{beverage[0]} 주문완료")
        total_Price += prices[0]
    elif menu_num == 2:
        print(f"{beverage[1]} 주문완료")
        total_Price += prices[1]

print(f"최종 금액 {total_Price}")