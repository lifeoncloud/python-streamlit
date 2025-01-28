menu = {"아메리카노": 2000, 
        "카페라떼": 2500, 
        "카푸치노": 2800, 
        "에스프레소": 2500, 
        "바닐라라떼": 3000,}

print("========메뉴========")
for name, price in menu.items():
    print(f"{name} : {price}원")
    
# 데이터 초기화
order_list = []

# 데이터에 한정이 있을 때 반복하면 for문 사용
# True일 때 반복하면 while문 사용
while True:
    selected_menu = input("주문하실 메뉴를 입력하세요(종료: q): ")
    if selected_menu == 'q' :
        break
    elif selected_menu not in menu :
        print("잘못된 메뉴입니다.")
    else :
        order_list.append(selected_menu)


total_price = sum(menu[menu_name] for menu_name in order_list)
print(total_price)

money = int(input(f"총 금액은 {total_price}입니다. 돈을 넣어주세요."))

if money >= total_price:
    change = money = total_price
    print(f"주문하신 내역은 {order_list}입니다. 거스릅돈은 {change}입니다.")


# 내 코드
# for menu_name in order_list:
#     total_price = total_price + menu[menu_name].valeus()



# # items, keys, values가 많이 쓰인다.
# print(menu.items())
# print(menu.keys())
# print(menu.values())
