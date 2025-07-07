#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Base URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    # Fetch user info
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

