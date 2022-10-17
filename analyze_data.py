import pandas as pd

df = pd.read_csv('college_students_hashtags.csv')

count = df['hashtag'].value_counts()
print(count)

count.to_csv('frequency_college_students_hashtags.csv')



