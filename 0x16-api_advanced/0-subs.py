#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query Reddit API and return number of subscribers for given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "SubredditSubscriberCounter"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                subscribers = data['data']['subscribers']
                return subscribers
            except KeyError:
                # Handle case when JSON response doesn't contain expected data
                return 0
        else:
            # Handle case when HTTP request fails
            return 0
    except requests.RequestException:
        # Handle case when there's an issue with the request
        return 0
