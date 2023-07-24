#!/usr/bin/python3
"""Fetches data from an API endpoint"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}todos?userId={argv[1]}&_expand=user"

    res = get(url).json()
    name = res[0]['user']['username']
    userId = res[0]['userId']
    with open(f"{userId}.csv", 'w', encoding="utf-8") as file:
        for todo in res:
            completed = todo['completed']
            title = todo['title']
            temp = f"\"{userId}\",\"{name}\",\"{completed}\",\"{title}\"\n"
            file.write(temp)
        file.close()
