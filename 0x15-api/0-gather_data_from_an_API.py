#!/usr/bin/python3
"""Fetches data from an API endpoint"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}todos?userId={argv[1]}&_expand=user"

    res = get(url).json()
    completed = [todo for todo in res if todo['completed']]
    name = res[0]['user']['name']
    print(f"Employee {name} is done with tasks({len(completed)}/{len(res)}):")
    for task in completed:
        print(f"\t {task['title']}")
