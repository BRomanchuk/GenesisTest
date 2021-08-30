import pandas as pd

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

sum_for_groups = df.sort_values(by='vals', ascending=False).groupby('grps').head(3).groupby('grps').sum()

print(sum_for_groups)