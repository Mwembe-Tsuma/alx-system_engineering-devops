#!/usr/bin/python3
"""
Python script that uses this REST API, foir a given employee ID
"""

import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python todo_progress.py <employee_id>")
    sys.exit(1)


base_url = "https://jsonplaceholder.typicode.com"
employee_id = int(sys.argv[1])


def get_todo(employee_id):
    """Send a GET request to retrieve the user's TODO list"""
    response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if response.status_code == 200:
        todos = response.json()
        done_tasks = [task for task in todos if task['completed']]
        tasks = len(todos)
        num_tasks = len(done_tasks)

        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()
        usr_name = user_data['name']

        print(f"Employee {usr_name} is done with tasks({num_tasks}/{tasks}):")
        for task in done_tasks:
            print("\t {}".format(task.get('title')))

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}")


if __name__ == "__main__":
    get_todo(employee_id)
