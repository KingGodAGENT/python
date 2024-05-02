# map(how, target): target을 바꿔주기
numList = [x for x in range(10)]
result = list(map(lambda x: x * 2, numList))
print(result)

# filter : target을 필터링해줌
result2 = list(filter(lambda x: x % 2 == 0, numList))
print(result2)

fruits = ['apple', 'banana', 'cherry', 'kiwi']
# 5글자 이하만 살리기
result3 = list(filter(lambda x: len(x) <= 5, fruits))
print(result3)

# 알파벳 a가 포함되어 있는거만 살리기
result4 = list(filter(lambda x: 'a' in x, fruits))
print(result4)

# map -> 유저아이디로 바꾸기
emailList = ["abc@naver.com", "mega@gmail.com", "korea@daum.net"]
result5 = list(map(lambda x: x.split("@")[0], emailList))
print(result5)