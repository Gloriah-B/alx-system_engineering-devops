#!/usr/bin/python3

"""
Module provides function to query the Reddit API and return the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns no of subscribers for given subreddit

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        Tuple[int, str]: A tuple containing number of subscribers for given
        subreddit and a message indicating if the subreddit exists.
    """
    # Reddit API endpoint for getting subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Custom User-Agent to prevent Too Many Requests error
    headers = {"User-Agent": "SubredditSubscriberCounter"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers'], "existing Subreddit"
        elif response.status_code == 404:
            return 0, "nonexisting subreddit"
        else:
            # Invalid subreddit or error occurred
            return 0, "error"
    except requests.RequestException:
        # Handle request exceptions (e.g., network error)
        return 0, "error"
