# 카페 판매 직원용 프로그램 개발 요청
'''
1. 커피판매 :
직원이 사용자 인터페이스를 통해 판매할 커피를 선택할 수 있습니다.
2. 커피 메뉴 추가 :
직원이 새로운 커피 종류를 메뉴에 추가할 수 있습니다.
3. 프로그램 종료 :
사용자가 프로그램을 종료할 수 있는 기능을 포함합니다.

예시:
1. 커피 판매
-> 아메리카노 2000원 2. 라떼 2500원 3. 바닐라라떼 3000원
2. 커피 메뉴 추가
-> 커피 이름 : ㅇㅇㅇ
-> 커피 가격 : ㅇㅇㅇ원
3. 프로그램 종료
'''

# 내가 짠것
# coffeeList = ['아메리카노', '라떼', '바닐라라떼']
# coffeeListPrice = ['2000', '2500', '3000']
#
# while True:
#     addCoffee = input("커피 이름: ")
#     addCoffeePrice = input("커피 가격: ")
#     print(f"커피 이름 : {addCoffee}, 커피 가격 : {addCoffeePrice}")
#     i = input("커피 메뉴 추가 Y/N ")
#     if i == "N" or i == "n":
#         break
#     elif i == "Y" or i == "y":
#         coffeeList.append(addCoffee)
#         coffeeListCost.append(addCoffeeCost)
#         print(f"{coffeeList}")

# 강사가 짠것
from coffee import Coffee

coffeeList = [Coffee("아메리카노", 2000, 100), Coffee("라떼", 2500, 150), Coffee("바닐라라떼", 3000, 50)]
while True:
    codeNumber = int(input("1.커피판매 2.커피추가 3.프로그램종료"))
    if codeNumber == 1:
        for i in coffeeList:
            print(i.intro())
        coffeeNumber = int(input("번호입력: "))
    elif codeNumber == 2:
        newCoffeeName = input("커피 이름: ")
        newCoffeePrice = int(input("커피 가격: "))
        newCoffeeCaffein = int(input("커피 카페인: "))
        coffeeList.append(Coffee(newCoffeeName, newCoffeePrice, newCoffeeCaffein))
        print(f"{newCoffeeName}이(가) 추가되었습니다")
    elif codeNumber == 3:
        print("프로그램 종료")
        break