#!/usr/bin/python3
"""Recursively counts keyword occurrences in hot post titles from a subreddit"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Counts occurrences of keywords in hot post titles of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:count.words:v1.0 (by /u/yourusername)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        # Normalize word list and initialize counts
        if not word_count:
            for word in word_list:
                key = word.lower()
                word_count[key] = word_count.get(key, 0)

        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in title:
                if word in word_count:
                    word_count[word] += 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, word_count)

        # Filter and sort results
        filtered = {k: v for k, v in word_count.items() if v > 0}
        for word in sorted(filtered.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word[0]}: {word[1]}")
    except Exception:
        return

