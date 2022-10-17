# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata

def create_csv():
    # Create file
    csvFile = open("college_students_hashtags.csv", "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    #Create headers for the data you want to save, in this example, we only want save these columns in our dataset
    csvWriter.writerow(['hashtag', 'tweet_id', 'tweet', 'created_at', 'geo', 'author_id' ,'lang', 'like_count', 'quote_count', 'reply_count','retweet_count'])


def append_to_csv(json_response, fileName):

    #A counter variable
    counter = 0

    #Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    #Loop through each tweet
    for tweet in json_response['data']:
        for hashtag in tweet['entities']['hashtags']:
            # 1. Author ID
            author_id = tweet['author_id']

            # 2. Time created
            created_at = dateutil.parser.parse(tweet['created_at'])

            # 3. Geolocation
            if ('geo' in tweet):   
                geo = tweet['geo']['place_id']
            else:
                geo = " "

            # 4. Tweet ID
            tweet_id = tweet['id']

            # 5. Language
            lang = tweet['lang']

            # 6. Tweet metrics
            retweet_count = tweet['public_metrics']['retweet_count']
            reply_count = tweet['public_metrics']['reply_count']
            like_count = tweet['public_metrics']['like_count']
            quote_count = tweet['public_metrics']['quote_count']

            # 8. Tweet text
            text = tweet['text']
            
            # 'hashtag', 'tweet_id', 'tweet', 'created_at', 'geo', 'author_id' ,'lang', 'like_count', 'quote_count', 'reply_count','retweet_count'
            res = [hashtag['tag'], tweet_id, text, created_at, geo, author_id, lang, like_count, quote_count, reply_count, retweet_count]
            
            # Append the result to the CSV file
            csvWriter.writerow(res)
        counter += 1

        # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added from this response: ", counter)