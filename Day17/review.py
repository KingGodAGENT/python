# 1. 문자열 잘라서 정렬하기
'''
ex)
myString            result
"axbxcxdx"          ["a","b","c","d"]
"dxccxbbbxaaaa"     ["aaaa","bbb","cc","d"]
'''

def solution1(myString):
    filteredList = list(filter(lambda i: i != "", myString.split("x")))
    filteredList.sort()
    return filteredList
print(solution1("axbxcxdx"))



# 2. 배열 원소 삭제하기
'''
ex)
arr                         delete_list                 result
[293,1000,395,678,94]       [94,777,104,1000,1,12]      [293,395,678]
[110,66,439,785,1]          [377,823,119,43]            [110,66,439,785,1]
'''
arr = [293,1000,395,678,94]
delete_list = [94,777,104,1000,1,12]

def solution2(arr, delete_list):
    return list(filter(lambda i: i not in delete_list, arr))
print(solution2([293,1000,395,678,94],[94,777,104,1000,1,12]))


# 3. 최댓값 만들기

'''
numbers                 result
[1,2,-3,4,-5]           15
[0,-31,24,10,1,9]       240
[10,20,30,5,5,20,5]     600
'''

def solution3(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]
print(solution3([1,2,-3,4,-5]))
