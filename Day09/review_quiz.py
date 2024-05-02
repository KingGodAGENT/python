# 이메일 주소 분리 퀴즈
'''
예시:
입력: "itKorea@naver.com"
출력: { user: "itKorea", domain: "naver.com" }
'''

# def splitEmail(email):
#     arr = email.split('@')
#     return {"user": arr[0], "domain": arr[1]}
#
# print(splitEmail(input("Enter your email address: ")))

# 문자열 변환 마법 퀴즈
'''
예시:
입력: "mega"
출력: {reversed: "agem", sorted: "aemg"}
'''
# def spellingMagic(word):
#     spellingList = list(word) # str에선 .sort가 안먹혀서 list화
#     spellingList.sort()
#     result = "".join(spellingList) # list -> str
#
#     spellingList2 = list(word)
#     spellingList2.reverse()
#     result2 = "".join(spellingList2) # list -> str
#     return {"reversed": result2, "sorted": result}
#
# print(spellingMagic("koreait"))

# 정수 n이 주어졌을때, 홀수면 "odd" 짝수면 "even"을 돌려주는 함수만들기

# def magic(num):
#     if num % 2 == 0:
#         return print("even")
#     else:
#         return print("odd")

