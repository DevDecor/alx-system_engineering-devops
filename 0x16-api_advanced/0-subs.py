#!/usr/bin/python3
"""Fetches the number of subscribers to a subreddit"""
import requests


def number_of_subscribers(subreddit) -> int:
    """Set a custom User-Agent to avoid Too Many Requests errors"""
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the URL for the subreddit's about.json endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        # response.status_code == 
        data = response.json()

        if data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
