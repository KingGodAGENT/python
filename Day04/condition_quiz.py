# 1. 정수를 입력 받아 양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수를 판별하는 프로그램
'''
예시: -5 -> 음의 홀수, 0 -> 0, 3-> 양의 홀수
'''

# num = int(input("정수 입력:"))
# if num > 0 and num % 2 == 0:
#     print("양의 짝수")
# elif num > 0 and num % 2 == 1:
#     print("양의 홀수")
# elif num < 0 and num % 2 == 0:
#     print("음의 짝수")
# elif num < 0 and num % 2 == 1:
#     print("음의 홀수")
# else:
#     print("0")


# num = int(input("정수 입력:"))
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0

# if isPositive and isodd:
#     print("양의 홀수입니다.")
# elif isPositive and isEven:
#     print("양의 짝수입니다.")
# elif isNegative and isOdd:
#     print("음의 홀수입니다.")
# elif isNegative and isEven:
#     print("음의 짝수입니다.")
# else:
#     print("0입니다.")


# 2. 좌표 평면에서 위치 판별 프로그램
'''
예시 
사용자 입력: 2,3
프로그램 출력: 입력하신 좌표는 제1사분면에 위치합니다.
'''

# x = float(input("x축 좌표:"))
# y = float(input("y축 좌표:"))

# if x == 0 and y == 0:
#     print("원점에 위치합니다")
# if x == 0 and y != 0:
#     print("y축위에 위치합니다")
# if x != 0 and y == 0:
#     print("x축위에 위치합니다")
# if x > 0 and y > 0:
#     print("입력하신 좌표는 제1사분면에 위치합니다")
# if x < 0 and y > 0:
#     print("입력하신 좌표는 제2사분면에 위치합니다")
# if x < 0 and y < 0:
#     print("입력하신 좌표는 제3사분면에 위치합니다")
# if x > 0 and y < 0:
#     print("입력하신 좌표는 제4사분면에 위치합니다")

# x = float(input("x 좌표 입력"))
# y = float(input("y 좌표 입력"))
# isXPositive = x > 0
# isYPositive = y > 0
# isXZero = x == 0
# isYZero = y == 0
# isXNegative = x < 0
# isYNegative = y < 0

# if isXZero and isYZero:
#     print("원점입니다")
# elif isYZero:
#     print("x축 위에 존재합니다")
# elif isXZero:
#     print("y축 위에 존재합니다")
# elif isXPositive and isYPositive:
#     print("1사분면 위에 존재합니다")
# elif isXNegative and isYNegative:
#     print("2사분면 위에 존재합니다")
# elif isXNegative and isYNegative:
#     print("3사분면 위에 존재합니다")
# else:
#     print("4사분면 위에 존재합니다")


# 3. 마트 할인 적용 프로그램
'''
예시
사용자 입력: 
150000
프로그램 출력: 
원래 상품 금액은 150000원, 할인율은 10%, 할인 금액은 15000원, 최종 결제 금액은 136000원입니다.
'''

price = int(input("원래 상품 가격:"))

if price >= 200000:
    print(f"원래 상품 금액은 {price}원, 할인율은 20%, 할인 금액은 {price*0.2}원, 최종 결제 금액은 {price-price*0.2}원입니다.")
elif price >= 100000:
    print(f"원래 상품 금액은 {price}원, 할인율은 10%, 할인 금액은 {price*0.1}원, 최종 결제 금액은 {price-price*0.1}원입니다.")
elif price >= 50000:
    print(f"원래 상품 금액은 {price}원, 할인율은 5%, 할인 금액은 {price*0.05}원, 최종 결제 금액은 {price-price*0.05}원입니다.")
else:
    print(f"원래 상품 금액은 {price}원, 할인율은 0%, 할인 금액은 {price*0}원, 최종 결제 금액은 {price-price*0}원입니다.")

