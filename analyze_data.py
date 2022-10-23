from webbrowser import get
import pandas as pd

def get_value_counts(filename):
    df = pd.read_csv("hashtag_csv/"+filename)

    count = df['hashtag'].value_counts()
    print(count.head(10))

    count.to_csv("frequencies/"+filename)

