#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
"""

from requests import get


def count_words(subreddit, word_list=[], after=None, cleaned_dict=None):
    temp = []

    for word in word_list:
        temp.append(word.casefold())

    cleaned_word_list = list(dict.fromkeys(temp))

    if cleaned_dict is None:
        cleaned_dict = dict.fromkeys(cleaned_word_list)

    params = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    url = 'https://www.r eddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                   after)

    response = get(url, headers=user_agent, params=params)

    if (response.status_code != 200):
        return None

    all_data = response.json()
    raw1 = all_data.get('data').get('children')
    after = all_data.get('data').get('after')

    if after is None:
        new = {k: val for k, val in cleaned_dict.items() if val is not None}

        for k in sorted(new.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(k[0], k[1]))
        return None

    for t in raw1:
        title = t.get('data').get('title')

        split_title = title.split()

        split_title2 = [t.casefold() for t in split_title]

        for j in split_title2:
            if j in cleaned_dict and cleaned_dict[j] is None:
                cleaned_dict[j] = 1

            elif j in cleaned_dict and cleaned_dict[j] is not None:
                cleaned_dict[j] += 1
    count_words(subreddit, word_list, after, cleaned_dict)
