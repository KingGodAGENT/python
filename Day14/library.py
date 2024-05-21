import math
import random

# print(random.randint(0,10000)


# 랜덤으로 여섯개의 숫자를 뽑아주는 프로그램 [1~45] 중복X

# lotto = []
#
# while True:
#     number = random.randint(1, 46)
#     if lotto.count(number) == 0:
#         lotto.append(number)
#         if len(lotto) == 6:
#             break
# lotto.sort()
# print(lotto)


# print(random.choice([1,2,3,4,5,6,7,8,9]))

# 6개 번호 유저에게 입력받아서 로또 몇등인지 알려주는 프로그램

lotto = []

while True:
    number = random.randint(1, 46)
    if lotto.count(number) == 0:
        lotto.append(number)
        if len(lotto) == 6:
            break
lotto.sort()

yourNumber = [int(input(f"{i}. 번호 입력: ")) for i in range(6)]
rank = 6
for i in lotto:
    if yourNumber.count(i) > 0:
        rank -= 1
print(f"로또: {lotto}")
print(f"당신: {yourNumber}")
print(f"{rank}등 축하드립니다!")


