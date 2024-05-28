import random
import pandas
from faker import Faker
f = Faker('ko_KR')


# 300명
teamlist = ["영업부", "사업부", "개발부", "경영부", "인사부", "생산부"]
agelist = [20,30,40,50,60]

data = {
    'name': [f.name() for i in range(300)],
    'age': [random.choice(agelist) for i in range(300)],
    'salary': [(random.randint(3000,10000)) // 500 * 500 for i in range(300)],
    'department': [random.choice(teamlist) for i in range(300)],
    'years_at_company': [random.randint(1,15) for i in range(300)],
    'job_satisfaction': [random.randint(1,10) for i in range(300)],
    'performance_score': [random.randint(1,100) for i in range(300)]
}

st = pandas.DataFrame(data)
print(st)
st.to_csv('company.csv', index=False, encoding='cp949')