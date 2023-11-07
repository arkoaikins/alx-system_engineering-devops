#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function that queries the Reddit API and returns a list
    containingthe titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "vagrant_ubuntu"}

    params = {"after": after}
    data = requests.get(url, headers=headers, allow_redirects=False,
                        params=params)
    if data.status_code == 200:
        after = data.json().get("data").get("after")
        post = data.json().get("data").get("children")
        for articles in post:
            hot_list.append(articles.get("data").get("title"))

        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    elif data.status_code == 404:
        return None
