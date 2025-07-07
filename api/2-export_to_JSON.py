#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Fetch user info
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Build JSON structure
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks}

    # Write to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile)
