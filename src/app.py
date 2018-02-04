import requests
import json
import csv
import random
import os


"""
Changes the script to the directory
it is running from. This allows the
use of relative file paths.
"""
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


CHANNEL_URL = os.environ['BORAT']
TWEET_CSV = 'devops_borat_tweets.csv'
headers = {
        'Content-Type': 'application/json',
        }


def create_data(tweet):
    """Creates the payload to be sent Hipchat"""
    data = {
            'color': 'purple',
            'message': f'{tweet}',
            'notify': False,
            'message_format': 'text',
            }

    return(data)


def get_tweet(csv_file):
    """Opens the csv file and returns a random tweet"""
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        tweet = [t[2] for t in reader]

    return random.choice(tweet)


def post(url, data, headers):
    """Posts payload to the Hipchat URL"""
    requests.post(url, data=json.dumps(data), headers=headers)


def main():
    tweet = get_tweet(TWEET_CSV)
    data = create_data(tweet)
    post(CHANNEL_URL, data, headers)

if __name__ == '__main__':
    main()

