# 1. 태어난 년도로 띠 알아보기
'''
태어난 년도를 입력받아, 그 해에 해당하는 띠를 알려주는 기능 구현
12간지(띠)를 활용하여 태어난 년도를 입력하면 그 해의 띠를 반환하는 함수 작성
'''
def yearToZodiac(year):
    zodiac = {
        0:"원숭이",
        1:"닭",
        2:"개",
        3:"돼지",
        4:"쥐",
        5:"소",
        6:"호랑이",
        7:"토끼",
        8:"용",
        9:"뱀",
        10:"말",
        11:"양"
    }
    return zodiac[year % 12]
print(yearToZodiac(1996))


# 2. 숫자 뒤집기
'''
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태 돌려주는 solution함수 작성
ex) n이 12345면 [5,4,3,2,1]을 리턴합니다
'''
# str(12345) # 문자화
# list(str(12345)) # [1 2 3 4 5]
# reversed(str(12345)) # [5 4 3 2 1]

def makeReverseNumber(i):
    return list(map(lambda i: int(i), reversed(list(str(i)))))
print(makeReverseNumber(12345))


# 3. 짝수는 싫어요
'''
정수 n이 매개변수로 주어질 때, 
n 이하의 홀수가 오름차순으로 담긴 배열을 리턴하도록 solution 함수 작성
ex) n = 10이면, result는 [1,3,5,7,9]
'''


def solution(num):
    return [i for i in range(num + 1) if i % 2 == 1]
print(solution(15))


# 4. 랜덤을 사용해서 띠함수를 사용하여, 100개 띠들이 있는 리스트 만들기
import random

a = [yearToZodiac(random.randint(1996,2025)) for i in range(100)]
print(a)

# random.randint(0,100) # 범위 내 랜덤 숫자 뽑기
# random.choice(["콜라","사이다","환타"]) # 아무거나 뽑기
# random.shuffle(a) # 랜덤으로 섞기
# a = ["콜라","사이다","환타"]
# b = [6, 2, 1, 1]
# random.choices(a, weights=b, k=1000)

