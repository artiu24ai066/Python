import pandas as pd
from itertools import product

data = {
    'artist': ['Kohli', 'Kohli', 'Rohit', 'Dhoni', 'Rohit', 'Dhoni', 'Kohli'],
    'venue': ['Stadium A', 'Stadium B', 'Stadium A', 'Stadium A', 'Stadium B', 'Stadium B', 'Stadium B'],
    'date': ['2024-01-15', '2024-01-20', '2024-01-15', '2024-02-10', '2024-02-15', '2024-03-01', '2024-03-10']
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

wide_table = counts.pivot_table(index='year_month', columns=['artist', 'venue'], values='count', fill_value=0)

print(wide_table)
