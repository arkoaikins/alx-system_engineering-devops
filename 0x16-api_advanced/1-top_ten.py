#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot post listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """function that returns titles of first 10 hot posts in a
    subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "vagratn_ubuntu"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        post = data.get('data').get('children')
        for hot_post in post:
            print(hot_post.get('data').get('title'))
    elif response.status_code == 404:
        print("None")
