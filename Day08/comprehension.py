# comprehension
# [0:100]리스트 출력

'''
list = []

for i in range(101):
    list.append(i)
print(list)
'''

'''
print([i for i in range(101)])
'''

# "apple" -> [a,p,p,l,e]

'''
print([i for i in "apple"])
'''

# 필터링 컴프리헨션
# 0~10까지 짝수만 리스트

'''
print([i for i in range(11) if i % 2 == 0])
'''

# 0~100 홀수만 리스트

'''
print([i for i in range(101) if i % 2 == 1])
'''

# 0~100 짝수 제곱인 형태인 리스트
# [0, 4, 16, 36, 64, ....]

'''
print([i ** 2 for i in range(101) if i % 2 == 0])
'''

# 0~10 홀수에서 10을 더한 리스트

'''
print([i + 10 for i in range(11) if i % 2 == 1])
'''

# -> [5, 6, 4]  단어길이대로 숫자출력

'''
fruits = ["apple", "orange", "pear"]

print([len(i) for i in fruits])
'''

# 매핑 컴프리헨션
# 홀수는 10 짝수는 20 더하기
'''
print([i + 10 if i % 2 == 1  else i + 20 for i in range(101)])
'''


fruits = ["apple", "orange", "pear"]

# 5글자 이하면 글자의 길이로 나타내고, 아니면 대문자화 하기

'''
print([len(i) if len(i) < 6 else i.upper() for i in fruits])
'''