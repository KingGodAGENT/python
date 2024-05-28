import pandas

df = pandas.read_csv('company.csv', encoding='cp949')

grouped_department = df.groupby('department')
print(grouped_department.count())
print(grouped_department.value_counts())
print(grouped_department['age'].mean())
print(grouped_department['salary'].mean())
print(grouped_department['salary'].std())
print(grouped_department['salary'].value_counts())
