#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    base_url = get('https://jsonplaceholder.typicode.com/todos/')
    data = base_url.json()

    row = []
    user_response = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_response.json()

    for i in user_data:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as csv_file:
        writ = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)
