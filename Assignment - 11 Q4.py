import pandas as pd
import numpy as np
import random
df = pd.DataFrame({
    'John': [random.choice([True, False]) for _ in range(10)],
    'Judy': [random.choice([True, False]) for _ in range(10)]
})

party_days = df['John'] & df['Judy']

days_til_party = [None] * 10

next_party = -1
for i in range(9, -1, -1):
    if party_days[i]:
        next_party = i
        days_til_party[i] = 0
    elif next_party != -1:
        days_til_party[i] = next_party - i

df['days_til_party'] = days_til_party

print(df)
