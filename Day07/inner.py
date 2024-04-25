# "hello".upper() ->? HELLO
# [].append("사과") -> ["사과"]
# print, input, str, list, int, float, bool, ...

# length
# len: 문자열 또는 리스트의 길이를 알려주는 기능

# print(len("hello"))
# print(len("python"))
# print(len([2,3,5,7,1]))

# max, min
# print(max([2,3,5,7,1145,152]))
# print(min([2,3,5,7,1145,152]))

# sum
# print(sum([2,3,5,7,56]))

'''
영어 기사 스크랩 해오고, 단어 길이가 6글자 이상인 단어들만 출력하기
힌트 : "hello world".split("") -> ["hello", "world"]
'''

# news = "Price of Shine Muscat continues to fall due to increase in production and decrease in quality"
# word = news.split()
#
# for i in word:
#     if len(i) >= 6:
#         print(i)

'''
문자 길이가 5글자 이하이고 알파벳 a,e 포함되면 대문자로 출력하고, 그게 아니면 그 과일의 문자 길이를 출력
-> APPLE, 6, 6, MANGO
'''

fruits = ["apple", "banana", "cherry", "mango"]

for i in fruits:
    if len(i) <= 5 and ("a" in i or "e" in i):
        print(i.upper())
    else:
        print(len(i))