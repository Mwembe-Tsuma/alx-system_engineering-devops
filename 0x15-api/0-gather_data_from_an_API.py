#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
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
        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)

        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data['name']

        print(f"Employee {employee_name} is done with tasks\
              ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}")


if __name__ == "__main__":
    get_todo(employee_id)
