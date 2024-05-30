import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("bicycle.csv", encoding='cp949')


def change(i):
    return i.split('_')[0]

df['시작_대여소명'] = df['시작_대여소명'].apply(change)
data = df['시작_대여소명'].value_counts()

plt.rcParams['font.family'] = 'Malgun Gothic'  # 글자 깨져서 안 깨지게 폰트 변경

data.plot.pie()
plt.show()




