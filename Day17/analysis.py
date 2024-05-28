import pandas

df = pandas.read_csv("company.csv", encoding='cp949')
# 기본 열 뽑기
print(df['name']) # 하나 열
print(df[['name', 'age', 'salary']]) # 다중 열


# 조건으로 열 뽑기
print(df[df['salary'] >= 5000])
print(df[df['years_at_company'] >= 7])

a = df['salary'] >= 5000
b = df['years_at_company'] >= 7
print(df[a & b])

y = df['years_at_company'] >= 10
s = df['job_satisfaction'] >= 8
p = df['performance_score'] >= 80
print(df[y & s & p])


# 열 추가
df['test'] = 50
print(df)

# 5년이하 사원, 10년 이하 과장, 15년이하 부장

def makeRank(i):
    if i <= 5:
        return '사원'
    elif i <= 10:
        return '과장'
    else:
        return '부장'

# apply 함수
df['rank'] = df['years_at_company'].apply(makeRank)
print(df)

# 20점이하 - 권고사직, 50점이하 직급유지, 80점이하 보너스, 100점이하 승진

def makeRank1(i):
    if i <= 20:
        return '권고사직'
    elif i <= 50:
        return '직급유지'
    elif i <= 80:
        return '보너스'
    else:
        return '승진'

df['aaa'] = df['performance_score'].apply(makeRank1)

print(df.info())
print(df.describe())










