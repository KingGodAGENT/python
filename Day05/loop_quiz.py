# 1. 1~100까지의 총합을 나타내는 프로그램

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# 2. 유저에게 과일을 입력받고, 모음을 제거한 단어로 내타내기
'''
예시 :
입력 : apple
출력 : ppl
'''

fruits = input("과일입력: ")
word = ""

for i in fruits:
    if not i in 'aeiou':
        word += i
print(word)