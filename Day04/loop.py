# 반복문 [loop]
# for 반복문
# for 미지수 in range(n번):
# print, input, str, float, bool, type
# range(n) [0~n-1까지 순회해줘]

# for x in range(10):
#     print(f"{x}. hello world")

# num = int(input("몇번 실행할까요: "))
# for x in range(num):
#     print(f"{x}. hello world")

# 0~200까지 찍는 프로그램 만드세요
# for x in range(201):
#     print(x)

# 0~200까지 짝수만 찍는 프로그램
# for x in range(201):
#     if x % 2 == 0:
#         print(x)

# 0~1000 3의 배수만 찍는 프로그램
# for x in range(1001):
#     if x % 3 == 0 and x !=0:
#         print(x)

# 구구단
# 유저에게 몇단을 입력하면, 해당 단을 모두 보여주는 프로그램
# ex) 3 -> 3,6,9,12,15,18,21,24,27
num = int(input("구구단 몇단?: "))
for i in range(10):
    print(num * i)


