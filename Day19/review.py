# 1. 핸드폰 번호 가리기
'''
ex)
phone_number            return
'027778888'             '*****8888'
'01033334444'           '*******4444'
'''

def solution(number):
    a = ''
    for index, item in enumerate(list(number)):
        if len(number) - index <= 4: # 원래 숫자 나오기
            a += item
        else: # 맨처음부터 ~ 전체길이의 -4 까지
            a += '*'
    return a
print(solution('027778888'))


# 2. 영어가 싫어요
'''
ex)
numbers                         result
'onetwothreefourfivesix'        123456
'onefourzerosix'                1406
'''

def solition1(numberStr):
    numberDict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0
    }

    for i in list(numberDict.keys()):
        if i in numberStr:
            numberStr = numberStr.replace(i, str(numberDict[i]))
    return numberStr
print(solition1('onetwothreefourfivesix'))