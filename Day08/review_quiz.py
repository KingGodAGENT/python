# 1. 정수 n에 따른 수열 합산 퀴즈
'''
예시 :
입력 : n = 5
출력 : 결과 : 9 (1+3+5)
입력 : n = 6
출력 : 결과 : 56(2^2+4^2+6^2)
'''

# num = int(input("양의 정수를 입력하세요"))
# result = 0
#
# if num % 2 == 1:
#     for i in range(num+1):
#         if i % 2 == 1:
#             result += i
# else:
#     for i in range(num+1):
#         if i % 2 == 0:
#             result += i ** 2
# print(result)


# 2. 배열 변환 기반 조건적 연산 퀴즈
'''
예시
입력: arr = [1,2,3](변수 선언 상태), k = 3(입력)
출력: 결과:[3,6,9] (모든 원소에 k값을 곱함)
입력: arr = [1,2,3](변수 선언 상태), k = 2(입력)
출력: 결과:[3,4,5] (모든 원소에 k값을 더함)
'''

# arr = [1,2,3]
# k = int(input("자연수 k 값 입력"))
#
# if k % 2 == 1:
#     for i in range(len(arr)):
#         arr[i] = arr[i] * k
# else:
#     for i in range(len(arr)):
#         arr[i] = arr[i] + k
# print(arr)

# arr = [1,2,3]
# k = int(input("자연수 k 값 입력"))
# newList = []

# if k % 2 == 1:
#     for i in arr:
#         newList.append(i * k)
# else:
#     for i in arr:
#         newList.append(i + k)
# print(newList)



