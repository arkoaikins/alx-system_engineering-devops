#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of all
hot articles,and prints a sorted count of given keywords
(case-insensitive,delimited by spaces.Javascript should count as
javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, kwargs={}, after=None):
    """
    function that queries the Reddit API,parses the title of all hot articles
    and prints a sorted count of given keywords
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
            lists = articles.get("data").get("title").lower().split()
            for words in lists:
                if words in word_list:
                    if words in kwargs:
                        kwargs[words] += 1
                    else:
                        kwargs[words] = 1
        if after:
            count_words(subreddit, word_list, kwargs, after)
        else:
            sorted_dict = {k: v for k,
                           v in sorted(kwargs.items(),
                                       key=lambda item: item[1])}
            [print("{}: {}".format(k, v)) for k, v in sorted_dict.items()]
    else:
        return None
