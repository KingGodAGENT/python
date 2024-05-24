# pandas 라이브러리 설치
import pandas # 데이터분석 라이브러리
from faker import Faker
import random

f = Faker('ko_KR')
print(f.name())

# arr = [i for i in range(101)]
# series = pandas.Series(arr)

# 길이 매칭 안맞아서 에러뜸
# data = {
#     'movies': ["혹성탈출", "범죄도시4", "설계자", "퓨리오사"],
#     'popcorn': ["오리지널 팝콘", "어니언 팝콘", "캬라멜 팝콘", "치즈 팝콘", "소금 팝콘"],
#     'beverage': ["콜라", "제로콜라", "사이다", "제로사이다", "환타", "탄산수", "에이드"]
# }
# df = pandas.DataFrame(data) # 엑셀화
# print(df)


# 학생이름 학년 전공 평균학점 10명

# studentdata = {
#     'name': ['김', '이', '박', '제갈', '한', '엄', '길', '최', '황', '정'],
#     'grade': [1,2,3,1,2,3,1,3,4,3],
#     'major': ['경영','경제','컴퓨터','미술','자동차','전기','전자','회계','비서','체육'],
#     'score': [3.5, 3.0, 3.0, 4.0, 2.0, 3.5, 3.9, 3.6, 4.2, 4.3]
# }
# a = pandas.DataFrame(studentdata)
# print(a)


# 학생 1000명

majorlist = ['경영','경제','컴퓨터','미술','자동차','전기','전자','회계','비서','체육','물리','화학','간호','무역','정치외교']
# def makename(): # 3자리 알파벳 랜덤 출력 함수 # 복잡함!! Faker로 쉽게 대체
#     return random.choice(list('abcdefghijklmnopqrstuvwxyz')) + random.choice(list('abcdefghijklmnopqrstuvwxyz')) + random.choice(list('abcdefghijklmnopqrstuvwxyz'))

stddata = {
    'name' : [f.name() for i in range(1000)],
    'grade' : [random.randint(1,5) for i in range(1000)],
    'major' : [random.choice(majorlist) for i in range(1000)],
    'score' : [round(random.uniform(0, 4.5), 2) for i in range(1000)]
}
st = pandas.DataFrame(stddata)
print(st)
st.to_csv('university.csv', index=False, encoding='cp949')

