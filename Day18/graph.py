import matplotlib.pyplot as plt
import pandas


# x : age
# y : salary
df = pandas.read_csv('company.csv', encoding='cp949')
x = df['age']
y = df['salary']

salary = df['salary'].value_counts()
satisfaction = df['job_satisfaction'].value_counts()

plt.hist2d(x,y)
plt.show()


