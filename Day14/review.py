# 1. 제일 작은 수 제거하기
'''
arr             return
[4,3,2,1]       [4,3,2]
[10]            [-1]
'''

# def solution(arr):
#     if len(arr) == 1:
#         return [-1]
#     else:
#         arr.remove(min(arr))
#         return arr
# print(solution([4, 3, 2, 1]))
# print(solution([10]))


# 2. 문자열 섞기
'''
str1         str2         str3
"aaaaa"     "bbbbb"      "ababababab"
'''

# def solution1(str1, str2):
#     text = ""
#     for i in range(len(str1)):
#         text += str1[i]
#         text += str2[i]
#     return text
# print(solution1("aaaaa","bbbbb"))


# 3. x 사이의 개수
'''
myString            result
"oxooxoxxox"        "1, 2, 1, 1"
"xabcxdefxghi"      "3, 3, 3"
'''

# def solution3(str):
#     return list(map(lambda x: len(x), filter(lambda x: len(x) > 0, str.split("x"))))


# 5. 5명씩
'''
names                                                           result
["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]      ["nami", "vex"]
'''

# arr = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
#
# def solution4(arr):
#     return [item for index, item in enumerate(arr) if index % 5 == 0]

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "소리 내는중"

class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)  # super은 부모를 지칭 즉 여기선 애니멀 클래스
        self.bread = bread

    def speak(self):
        return f"{super().speak()} ... 멍멍"

a = Dog("John", "하얀개")
print(a.speak())

