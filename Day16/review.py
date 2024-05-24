# 1. 조건에 맞게 수열 변환하기
# 정수 배열 arr와 자연수 k가 주어짐.
# k가 홀수라면 arr * k, k가 짝수라면 arr + k
# 함수 solution
'''
arr                     k       result
[1,2,3,100,99,98]       3       [3,6,9,300,297,294]
[1,2,3,100,99,98]       2       [3,4,5,102,101,100]
'''


def solution(k, arr):
    return [i * k if k % 2 == 1 else i + k for i in arr]
print(solution(2, [1,2,3,100,99,98]))


# 2. A강조하기
'''
문자열 myString이 주어짐.
myString에서 알파벳 'a'가 등장하면 전부 'A'로 변환하고,
'A'가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 retutn하는 solution1함수 작성
'''

def solution1(myString):
    return "".join(['A' if i == 'a' else i.lower() for i in myString])
print(solution1('asdASDasddgsdGDF'))


# 3. 오늘 날짜 05-24, 05-25, ...,06-24 까지 담긴 리스트를 문자열로 출력

import datetime

def solition2(i):
    today = datetime.date.today()
    future = today + datetime.timedelta(days = i)
    return future.strftime("%m-%d")
print([solition2(i) for i in range(31)])