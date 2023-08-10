#!/usr/bin/python3
"""Fetches the top 10 poats of a subreddit"""
import requests


def top_ten(subreddit) -> int:
    """Set a custom User-Agent to avoid Too Many Requests errors"""
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the URL for the subreddit's about.json endpoint
    url = f'https://www.reddit.com/r/{subreddit}/top.json'
    params = {'limit': 10, 'sort': 'top'}
    try:
        response = requests.get(url, params=params, headers=headers, allow_redirects=True)
        # response.status_code == 
        data = response.json()
        if data and 'children' in data['data']:
           posts = data['data']['children']
           [print(post["data"]["title"]) for post in posts]
        else:
            print(None)
    except requests.RequestException:
        print(None)
