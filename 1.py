import numpy as np
import pandas as pd

data = {
    'A': np.random.randint(1, 100, 10),
    'B': np.random.rand(10),
    'C': np.random.choice(['X', 'Y', 'Z'], 10)
}

df = pd.DataFrame(data)

df['D'] = df['A'] * df['B']
df['E'] = df['D'].apply(lambda x: 'High' if x > 50 else 'Low')

mean_A = df['A'].mean()
sum_B = df['B'].sum()
unique_C = df['C'].unique()

filtered_df = df[df['A'] > 50]

grouped_df = df.groupby('C').agg({'A': 'mean', 'B': 'sum'})

print(df)
print(mean_A)
print(sum_B)
print(unique_C)
print(filtered_df)
print(grouped_df)
