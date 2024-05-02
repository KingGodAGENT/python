# list_type
'''
soccerPlayer = ["손흥민","황희찬","김민재","이강인"]
soccerPlayer.append("이재성")
soccerPlayer.sort()
print(soccerPlayer)
'''



# 유저에게 과일을 영어로 3개 입력받고, 과일리스트를 만든 후 대문자화, 오름차순으로 출력하기

'''
a = input("첫번째 과일: ")
b = input("두번째 과일: ")
c = input("세번째 과일: ")
upperA = a.upper()
upperB = b.upper()
upperC = c.upper()
fruits = []
fruits.append(upperA)
fruits.append(upperB)
fruits.append(upperC)
fruits.sort()
print(fruits)
'''

'''
fruitsList = []
for i in range(3):
    fruits = input("과일 입력:")
    fruitsList.append(fruits.upper())
fruitsList.sort()
print(fruitsList)
'''