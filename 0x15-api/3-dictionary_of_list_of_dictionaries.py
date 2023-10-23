#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    base_url = get('https://jsonplaceholder.typicode.com/todos/')
    data = base_url.json()

    row = []
    user_response = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_response.json()

    dict1 = {}
    for j in user_data:
        row = []
        for i in data:
            dict2 = {}
            if j['id'] == i['userId']:
                dict2['username'] = j['username']
                dict2['task'] = i['title']
                dict2['completed'] = i['completed']
                row.append(dict2)

        dict1[j['id']] = row

    with open("todo_all_employees.json",  "w") as fd:
        json_obj = json.dumps(dict1)
        fd.write(json_obj)
