# 1. 음료 선택 및 잔돈 계산 프로그램
'''
음료의 종류를 나타내는 정수(1~3)와 투입할 금액을 나타내는 양의 정수를 입력
프로그램은 사용자가 선택한 음료와 투입한 금액에 따라,
음료의 이름과 잔돈을 계산하여 출력
'''
'''
americano = 3000
lemonade = 4000
late = 3500

a = int(input("음료를 선택하세요. 1:아메리카노 2:레몬에이드 3:카페라떼"))
cash = int(input("투입할 금액을 입력하세요:"))

if a == 1:
    print(f"아메리카노를 선택하셨습니다. 잔돈은 {cash-americano}입니다.")
elif a == 2:
    print(f"레몬에이드를 선택하셨습니다. 잔돈은 {cash-lemonade}입니다.")
elif a == 3:
    print(f"카페라떼를 선택하셨습니다. 잔돈은 {cash-late}입니다.")
'''

# 2. 버스 요금 계산 프로그램
'''
버스 노선의 종류를 나타내는 정수(1~3)와 승객의 나이를 입력받아,
노선과 연령에 따라 적용되는 할인을 반영한 최종 요금을 계산하여 출력
'''
'''
a = 1200
b = 2000
c = 1000
teen = 0.3

i = int(input("버스노선을 선택하세요. 1:시내버스 2:광역버스 3:마을버스"))
j = int(input("나이는?:"))

if i == 1 and j >= 8 and j < 20:
    print(f"시내버스 요금은 {1200 - teen * 1200}원 입니다.")
elif i == 1 and j <= 7 or j >= 65:
    print("시내버스 요금 무료")
elif i == 1 and j >= 20 and j < 65:
    print("시내버스 요금은 1200원입니다.")
elif i == 2 and j >= 8 and j < 20:
    print(f"광역버스 요금은 {2000 - teen * 2000}원 입니다.")
elif i == 2 and j <= 7 or j >= 65:
    print("광역버스 요금 무료")
elif i == 2 and j >= 20 and j < 65:
    print("광역버스 요금은 2000원입니다.")
elif i == 3 and j >= 8 and j < 20:
    print(f"마을버스 요금은 {1000 - teen * 1000}원 입니다.")
elif i == 3 and j <= 7 or j >= 65:
    print("마을버스 요금 무료")
elif i == 3 and j >= 20 and j < 65:
    print("마을버스 요금은 1000원입니다.")
'''

# 3. n의 배수중에 짝수만 100까지 출력

num = int(input("정수 입력: "))

for i in range(1,101):
    if i % num == 0 and i % 2 == 0:
        print(i)