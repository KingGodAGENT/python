# variable, input/print, dataType. operator
# 조건문[if-elif-else]
num = int(input("Enter a number: "))
if num > 0:
    print("0보다 큽니다.")
elif num == 0:
    print("0입니다.")
else:
    print("0보다 작습니다.")

# 반복분[for 문]
for i in range(100):
    if i % 2 == 0:
        print(i) #0,2,4,6,8...98
