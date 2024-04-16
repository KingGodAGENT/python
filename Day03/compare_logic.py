# compare[비교] : 결과는 bool 타입
# >. <. <=, >=, ==[같니?], !=[다르니?]

a = 10
b = 20
print(a > b) # 초과 False
print(a >= b) # 이상 False
print(a < b) # 미만 True
print(a <= b) # 이하 True
print(a == b) # 동등 False
print(a != b) # 비동등 True


# logic[논리] 연산자 : bool타입에 사용되는 연산자
# and, or, not
c = 5
d = 3
# and : 모든 조건이 참이면 참
print(c > d and c == 5 and d == 3) # True
# or : 하나라도 조건이 참이면 참
print(c < d or c == 6 and d == 3) # True
# not : 조건의 반대를 반환
print(not(c > d)) # False


x = 5
result = x > 3 and x == 5 # True
# 드모르간 법칙 적용
result1 = not(x <= 3) or not(x != 5)


