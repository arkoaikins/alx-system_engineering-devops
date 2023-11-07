#!/usr/bin/python3
"""
Function the queries the Reddit API and returns the number
of subscribers for a given subreddit,if an invalid subreddit
is given function returns 0
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total number of subsribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "vagratn_ubuntu"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        no_ofsubs = data.get('data').get('subscribers')
        return no_ofsubs
    elif response.status_code == 404:
        return 0
