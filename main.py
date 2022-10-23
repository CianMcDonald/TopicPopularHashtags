from analyze_data import get_value_counts
from csv_handler import create_csv
from twitter_handler import run_twitter_search


def main():
    keyword = "inflation -is:retweet -is:reply has:hashtags lang:en"
    filename = "inflation.csv"
    create_csv(filename)
    run_twitter_search(keyword, filename)
    get_value_counts(filename)


if __name__ == '__main__':
    main()