#!/usr/bin/python3
"""Fetches data from an API endpoint"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    from json import dump

    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}todos?userId={argv[1]}&_expand=user"

    res = get(url).json()
    tasks = {f"{argv[1]}": []}
    array = tasks[f"{argv[1]}"]
    name = res[0]['user']['username']
    userId = res[0]['userId']
    with open(f"{userId}.json", 'w', encoding="utf-8") as file:
        for todo in res:
            todoDict = dict()
            todoDict['task'] = todo['title']
            todoDict['completed'] = todo['completed']
            todoDict['username'] = name
            array.append(todoDict)
        dump(tasks, file)
        file.close()
