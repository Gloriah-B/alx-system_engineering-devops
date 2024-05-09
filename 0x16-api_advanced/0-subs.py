#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of subscribers for given subreddit

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the given subreddit.
        Returns 0 if the subreddit is invalid.
    """

    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to prevent Too Many Requests error
    headers = {
        "User-Agent": "SubredditSubscriberCounter"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Invalid subreddit or error occurred
            return 0
    except requests.RequestException:
        # Handle request exceptions (e.g., network error)
        return 0
