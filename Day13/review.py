# 1. 문자열 뒤집기
'''
문자열 my_string이 매개변수로 주어집니다.
my_string을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성하기
'''

# def reversedWord(my_string):
#     wordList = list(my_string) # [k,o,r,e,a]
#     wordList.reverse() # [a,e,r,o,k]
#     reversedWord = "".join(wordList) # aerok
#     return reversedWord


# 2. 미완성된 할 일 찾기
'''
todo_list에 있는 할 일 중,
finished 배열을 통해 아직 끝내지 못한 일들을 찾아 순서대로 배열에 담아 반환하는 함수 만들기
'''


# todoList = ["swim", "problemsolving", "study", "practiceguitar"]
# doneList = [True, False, True, False]
#
# def filterDoneList(todoList, doneList):
#     return [item for index, item in enumerate(todoList) if doneList[index] == True]

class Animal:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def eat(self):
        print("냠냠냠")

    def sound(self):
        pass

    def introduce(self):
        print(f"이름:{self.name} 종:{self.bread}")

class Dog(Animal):
    def sound(self):
        print("멍멍")

# 고양이 eat 냠냠냠 sound 냐옹
class Cat(Animal):
    def sound(self):
        print("냐옹")


# 퀴즈
# 관리자, 편집자, 뷰어 라는 각각 사용자가 존재합니다
# 모두 접근하기라는 함수를 가지고 있습니다
# 모두 username이라는 속성도 가지고 있습니다

# 관리자 - 유저만들기
# 편집자 - 편집하기
# 뷰어 - 조회하기

class user:
    def __init__(self, username):
        self.username = username

    def access(self):
        pass

class admin(user):
    def access(self):
        print("관리자가 접근합니다")

    def createuser(self):
        print("유저 생성")

class editor(user):
    def access(self):
        print("편집자가 접근합니다")

    def edit(self):
        print("편집하기")

class viewer(user):
    def access(self):
        print("뷰어가 접근합니다")

    def inquiry(self):
        print("조회하기")
