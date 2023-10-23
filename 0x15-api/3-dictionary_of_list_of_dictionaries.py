#!/usr/bin/python3
"""
Extention of task 0 script to export data in CSV format
Records all tasks from all employees
 """
import json
import requests


def fetch_employee_data(user_id, todos):
    taskList = []
    for task in todos:
        if task.get('userId') == user_id:
            taskDict = {
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            taskList.append(taskDict)
    return user_id, taskList


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data.")
        exit(1)

    users = users_response.json()
    todos = todos_response.json()
    todoAll = {}

    for user in users:
        user_id, taskList = fetch_employee_data(user.get('id'), todos)
        todoAll[user_id] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
