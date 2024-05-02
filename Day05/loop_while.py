# loop_while

# i = 10
# while i > 0:
#     print("야호")
#     i -= 1

# i = -1
# while i != 0:
#     i = int(input("숫자 0을 넣어야 멈춤:"))

# while True:
#     i = int(input('숫자 0을 넣어야 멈춤: '))
#     if i == 0:
#         break

# 숫자 0넣으면 멈추고, 1을 입력하면 아메리카노가 출력되고, 2를 입력하면 라떼가 출력되는

# while True:
#     coffee = int(input("0넣으면 멈추고 1을 입력하면 아메리카노, 2를 입력하면 라떼"))
#     if coffee == 0:
#         break
#     elif coffee == 1:
#         print("아메리카노")
#     elif coffee == 2:
#         print("라떼")

# 1입력시 python출력, 2 java, 3 c++, 4 프로그램 종료, 그 외 숫자는 잘못입력하셨습니다.

# while True:
#     i = int(input('1은 python, 2는 java, 3은 c++, 4는 종료: '))
#     if i == 1:
#         print("python")
#     elif i == 2:
#         print("java")
#     elif i == 3:
#         print("c++")
#     elif i == 4:
#         break
#     else:
#         print("잘못 입력하셨습니다.")

# 계산기 프로그램
'''
예시 :
사용자 입력: 0
프로그램 출력: 프로그램 종료
사용자 입력: 1
프로그램 출력: 더하기
사용자 입력: 2
프로그램 출력: 빼기
사용자 입력: 3
프로그램 출력: 곱하기
사용자 입력: 4
프로그램 출력: 제곱
사용자 입력: 5
프로그램 출력: 나누기(몫)
그외 번호는 번호 입력 오류 -> 다시묻기
'''

while True:
    print("계산기 프로그램")
    num1 = int(input("첫번째 숫자 입력:"))
    num2 = int(input("두번째 숫자 입력:"))
    num = int(input("0은 종료, 1은 더하기, 2는 빼기, 3은 곱하기, 4는 제곱, 5는 나누기(몫), 그외는 입력오류"))
    if num == 0:
        print("계산기 프로그램 종료")
        break
    elif num == 1:
        print(f"{num1 + num2}")
    elif num == 2:
        print(f"{num1 - num2}")
    elif num == 3:
        print(f"{num1 * num2}")
    elif num == 4:
        print(f"{num1 ** num2}")
    elif num == 5:
        print(f"{num1 // num2}")
    else:
        print("입력오류")

