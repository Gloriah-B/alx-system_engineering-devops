#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ Query Reddit API and return no of subscribers for given subreddit"""


url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 200:
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
else:
    return 0
