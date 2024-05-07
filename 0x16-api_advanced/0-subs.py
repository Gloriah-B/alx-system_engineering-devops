#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query Reddit API and return number of subscribers for given subreddit.

    Args:
    - subreddit (str): The name of the subreddit to query.

    Returns:
    - int: The number of subscribers for the given subreddit. Returns 0 if
    the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "SubredditSubscriberCounter"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0
