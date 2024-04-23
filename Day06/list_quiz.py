# 1. 유저에게 다섯개의 정수를 입력받고, 리스트화 한 다음에 각각 요소를 3배로 만든다음 출력
# ex) [4,1,5,6,2] -> [12,3,15,18,6]
'''
numberslist = []
for x in range(5):
    num = int(input("정수 입력: "))
    numberslist.append(num)
print(numberslist)

newnumberslist = []
for x in numberslist:
    newnumberslist.append(x*3)
print(newnumberslist)
'''
# list = [num1*3, num2*3, num3*3, num4*3, num5*3]
# print(list)

# 2. 유저에게 서로 다른 다섯개의 정수를 입력받고, 리스트화 한 다음에 가장 큰 수를 뽑아내는 프로그램
'''
numberslist = []
for x in range(5):
    num = int(input("정수 입력: "))
    numberslist.append(num)
numberslist.sort()
numberslist.reverse()
print(numberslist[0])
'''






