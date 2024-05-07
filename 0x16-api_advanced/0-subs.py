#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ Query Reddit API and return no of subscribers for given subreddit"""

    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to prevent Too Many Requests error
    headers = {
        "User-Agent": "SubredditSubscriberCounter"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the response contains subreddit data
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        # Handle any request exceptions, such as network errors
        return 0

# Example usage:
# print(number_of_subscribers("python"))
