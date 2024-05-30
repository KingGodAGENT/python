# 1. 문자열 섞기
'''
문자열 my_str과 n이 매개변수로 주어질 때,
my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution함수 만들기
ex)
my_str                  n           result
'abcdef123'             3           ['abc', 'def', '123']
'abc1Addfggg4556b'      6           ['abc1Ad', 'dfggg4', '556b']
'''

def solution(my_str, n):
    arr = []
    word = ''
    for index, item in enumerate(my_str, 1):
        word += item
        if index % n == 0:
            arr.append(word)
            word = ''
    arr.append(word)
    return arr
print(solution('abc1Addfggg4556b', 6))








# 2. JadenCase 문자열 만들기
'''
JadenCase란 모든 단어의 첫문자가 대문자이고,
그 외의 알파벳은 소문자인 문자열입니다.
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면됩니다.
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 return하는 함수 solution1 작성
'''

def solution1(s):
    return ' '.join([i.capitalize() for i in s.split(' ')])

print(solution1('for the last week'))

