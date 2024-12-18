import pandas as pd
data = {
    "Values": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
df['Cumulative Sum'] = df['Values'].cumsum()
print("Обновленный DataFrame с накопительной суммой:")
print(df)