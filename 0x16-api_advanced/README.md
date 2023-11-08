# API advanced :page_with_curl: 0x16. API advanced
## In this project :bulb:
## Overview
- This is an API project where i use Reddit API for some practice
  - The Reddit API has lot's of endpoints,many that don't require autentication,
    and there are ton's of information to be parsed out and presented
- This project helps me to get comfortable with API calls
## Requirements of the project
- Used Vi/Vim editor
- Files are compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- Codes use PEP 8 style
- all modules have documention`(python3 -c 'print(__import__("my_module").__doc__)')`

### Resources
[Reddit API Documentation](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA)

[Query String](https://intranet.alxswe.com/rltoken/luFn_zrgmAQ0OAO_PEI9bA)

### Task 0
Write a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid subreddit is given,
the function should return 0.
- Requirements
   - Prototype: def number_of_subscribers(subreddit)
   - If not a valid subreddit, return 0.
Filename:`0-subs.py`
tested with:`0-main.py`
how to run: `python3 0-main.py programming` and `python3 0-main.py this_is_a_fake_subreddit`


### Task 1
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
- Requirements
  - Prototype: def top_ten(subreddit)
  - If not a valid subreddit, print None.
Filename:`1-top_ten.py`
tested with:`1-main.py`
how to run: `python3 1-main.py programming` and `python3 1-main.py this_is_a_fake_subreddit`

### Task 2
Write a recursive function that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results are found for the given
subreddit, the function should return None.
- Requirements:
  - Prototype: def recurse(subreddit, hot_list=[])
  -  You may change the prototype, but it must be able to be called with just a subreddit supplied.
     AKA you can add a counter, but it must work without supplying a starting value in the main.
  - If not a valid subreddit, return None
  - using a loop and not recursively calling the function! This /can/ be done with a loop
  but the point is to use a recursive function.
Filename:`2-recurse.py`
Tested with: `2-main.py`
how to run: `python3 2-main.py programming` and `python3 2-main.py this_is_a_fake_subreddit`

### Task 3
Write a recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
- Requirements
  - Prototype: def count_words(subreddit, word_list)
  - You may change the prototype, but it must be able to be called with just a subreddit supplied
  and a list of keywords. AKA you can add a counter or anything else, but the function must work without
  supplying a starting value in the main.
  - If word_list contains the same word (case-insensitive), the final count should be the sum of each
  duplicate (example below with java)
  - Results should be printed in descending order, by the count, and if the count is the same for separate
  keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should
  be skipped and not printed. Words must be printed in lowercase.
  - Results are based on the number of times a keyword appears, not titles it appears in. java java java counts
  as 3 separate occurrences of `java`.
  - To make life easier, java. or `java!` or `java_` should not count as `java`
  - If no posts match or the subreddit is invalid, print nothing.
  - using a loop and not recursively calling the function! This /can/ be done with a loop but the point
  is to use a recursive function.
Filename:`100-count.py`
Tested with: `100-main.py`
how to run: `python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'`
how to run: `python3 100-main.py programming 'JavA java'`
how to run: `python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'`
how to run: `python3 100-main.py not_a_valid_subreddit 'python java'`






