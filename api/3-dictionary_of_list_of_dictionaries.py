#!/usr/bin/python3
"""Exports all employees' TODO list data to a JSON file"""
import json
import requests

if __name__ == "__main__":
    # Base URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users and todos
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Build the final dictionary
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Filter todos for this user
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

        all_data[str(user_id)] = user_tasks

    # Write to JSON file
    with open("todo_all_employees.json", mode="w") as jsonfile:
        json.dump(all_data, jsonfile)
