# 1. 문자열 문자 반복 프로그램
'''
주어진 문자열 word의 각 문자를 정수 n만큼 반복하여 새로운 문자열을 생성하는 프로그램 작성
예시:
입력:word= "abc",n=3
결과:"aaabbbccc"
힌트:"kiwi"*2 -> "kiwikiwi" or for in for(for 안에 for문)
'''

# n = int(input("반복횟수:"))
# word = str(input("word="))
#
# newWord = ""
# for i in "abc":
#     newWord += i * 3
# print(newWord)


# 2. 모음 대문자화 프로그램
'''
입력: "hello world"
결과: "hEllO wOrld"
힌트: in 연산자, 문자열.upper()
'''

# word = input("입력:")
# newWord = ""
#
# for i in word:
#     if i in "aeiou":
#         newWord += i.upper()
#     else:
#         newWord += i
# print(newWord)


# 3. 문자열 대소문자 전환 프로그램
'''
입력: "cccCCC"
출력: "CCCccc"
입력: "abcdef"
출력: "ABCDEF"
힌트: isUpper or isLower -> upper(), lower()
'''

# word = input("문자 입력:")
# newWord = ""
#
# for i in word:
#     if i.islower():
#         newWord += i.upper()
#     else:
#         newWord += i.lower()
# print(newWord)

# 4. 자음만 대문자화
'''
단어를 입력했을때, 자음은 대문자화해서 출력
ex) hello -> HeLLo
'''

# word = input("단어 입력:")
# newWord = ""
#
# for i in word:
#     if i not in "aeiou":
#         newWord += i.upper()
#     else:
#         newWord += i
# print(newWord)