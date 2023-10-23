#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    base_url = get('https://jsonplaceholder.typicode.com/todos/')
    data = base_url.json()

    row = []
    user_response = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_response.json()

    for i in user_data:
        if i['id'] == int(argv[1]):
            employee = i['username']
            usr_id = i['id']

    row = []
    for i in data:

        new_dict = {}
        if i['userId'] == int(argv[1]):
            new_dict['username'] = employee
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            row.append(new_dict)

    result_dict = {}
    result_dict[usr_id] = row
    json_obj = json.dumps(result_dict)

    with open(argv[1] + ".json",  "w") as fd:
        fd.write(json_obj)
