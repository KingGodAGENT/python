import matplotlib.pyplot as plt
import pandas
import matplotlib.pyplot

df = pandas.read_csv('japan.csv')

# 2023년에 각 나라별 방문자 수를 알고 싶다!
year_2023 = df[(df['Year'] == 2023) & (df['Purpose_of_visit_to_Japan'] == 'Tourism')]
data = year_2023.groupby('Country/Area')['Visitor Arrivals'].sum() # 중국이 데이터 안에 숫자가 아닌 NaN을 넣어버려서 안됨

print(data)


