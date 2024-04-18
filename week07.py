#
beverage = ['Espresso','Compagina','Lemonade']
prices = [2000,2500,3900]
total_Price = 0
quantity = [0,0,0]



while True:
    for i in range(len(beverage)):
        print(f"{i+1}) {beverage[0]} : {prices[0]} \n")
    menu_num = int(input(f"{len(beverage)+1}) exit\n 메뉴를 입력하세요 : "))

    if menu_num == len(beverage)+1:
        print("주문확정")
        break
    elif menu_num == 1:
        print(f"{beverage[0]} 주문완료")
        total_Price += prices[0]
        quantity[0] +=1
    elif menu_num == 2:
        print(f"{beverage[1]} 주문완료")
        total_Price += prices[1]
        quantity[1] += 1
    elif menu_num == 3:
        print(f"{beverage[2]} 주문완료")
        total_Price += prices[2]
        quantity[2] += 1

print(f"움료\t가격\t수량\t{'소계':>6}\n")
for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\t{prices[i]}\t{quantity[i]}\t{prices[i]*quantity[i]:>6}\n")
print(f"최종 금액 {total_Price}")