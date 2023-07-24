#!/usr/bin/python3
"""Fetches data from an API endpoint"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    from json import dump

    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}users?_embed=todos"

    res = get(url).json()
    # print(res)
    tasks = dict()
    for user in res:
        name = user['username']
        for todo in user['todos']:
            todoDict = dict()
            todoDict['username'] = name
            todoDict['task'] = todo['title']
            todoDict['completed'] = todo['completed']
            if f"{user['id']}" not in tasks:
                tasks[f"{user['id']}"] = []
            tasks[f"{user['id']}"].append(todoDict)
    with open("todo_all_employees.json", 'w', encoding="utf-8") as file:
        dump(tasks, file)
        file.close()
