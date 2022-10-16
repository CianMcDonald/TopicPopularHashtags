import pandas as pd

df = pd.read_csv('cost_of_living_hashtags.csv')

count = df['hashtag'].value_counts(normalize=True)
print(count)

count.to_csv('frequency_col_hashtags.csv')



