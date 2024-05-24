# 메가커피 당일 매출 기록표

# 이름 메뉴 몇시 결제수단 매장/포장
import pandas # 데이터분석 라이브러리
from faker import Faker
import random
import datetime

f = Faker('ko_KR')

menulist = ['아아','뜨아','자몽에이드','블루베리스무디','플레인요거트스무디','쌍화차','라떼','카페모카']
cardcash = ['card', 'cash']

# def get_random_time():
#     opentime = datetime.datetime.strftime("07:00", "%H:%M")
#     closetime = datetime.datetime.strftime("22:00", "%H:%M")
#     total = int((closetime - opentime).total_seconds() / 60) # 전체 몇분
#     random_minutes = random.randint(0, total)
#     return opentime + datetime.timedelta(minutes=random_minutes)
# print(get_random_time().strftime("%H: %M"))   # 미완성


megacoffeedata = {
    'name' : [f.name() for i in range(5000)],
    'menu' : [random.choice(menulist) for i in range(5000)],

    'card' : [random.choice(cardcash) for i in range(5000)],
    'here' : [random.choice(["포장", "매장"]) for i in range(5000)]
}
st = pandas.DataFrame(megacoffeedata)
st.to_csv('megacoffee.csv', index=False, encoding='cp949')


