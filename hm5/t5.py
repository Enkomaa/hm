import pandas as pd
import numpy as np
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}
#Задание 1
df = pd.DataFrame(data)
print('Задание 1')
print(df)
print()
#Задание 2
print('Задание 2')
print(df[(df['GPA'] > 3.7) & (df['Department'] == 'Math')])
print()
#Задание 3
print('Задание 3')
print(df.sort_values(by = 'Age'))
print()
print(df.sort_values(by = 'GPA', ascending=True))
print()
#Задание 4
print('Задание 4')
print(df['GPA'].mean())
print()
print(df.groupby('Department')['Name'].count())
print()
#Задание 5
print('Задание 5')
df['Internship'] = [True, False, np.nan, True, np.nan]
missing_values = df[df['Internship'].isna()]
df['Internship'].fillna(False, inplace=True)
print("DataFrame с добавленным столбцом Internship:")
print(df)
print("\nСтроки с пропущенными значениями:")
print(missing_values)
print()
#Задание 6
print('Задание 6')
df['Final Credits'] = df['Credits'] * df['GPA']
print(df)
print()
#Задание 7
print('Задание 7')
second_student = df.iloc[1]
print("Данные о втором студенте:")
print(second_student)
first_three_students = df.iloc[:3, [0, 3]]
print("\nИмена и баллы GPA первых трёх студентов:")
print(first_three_students)
df.iloc[3, 3] = 3.95
print("\nИзменение GPA четвёртого студента:")
print(df)
ltc = df.iloc[:, -2:]
print("\nПоследние два столбца для всех студентов:")
print(ltc)