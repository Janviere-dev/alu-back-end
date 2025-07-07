#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to CSV format"""
import csv
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

    # Write to CSV
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
