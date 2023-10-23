#!/usr/bin/python3
"""
Extention of task 0 script to export data in CSV format
Records all tasks that are owned by this employee

 """
import csv
import json
from requests import Session
import sys

if __name__ == "__main__":

    s = Session()

    # URL's to get employee's tasks and name
    user_id = sys.argv[1]
    emp_tasks = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)
    emp_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # HTTP requests to the API via the URLS to get employee tasks and name
    # and parsing the JSON response
    employee_todo = (s.get(emp_tasks)).json()
    employeeName = (s.get(emp_name)).json()['username']

    totalTasks = []

    for emp_task in employee_todo:
        task = emp_task.get('title')
        completed = emp_task.get('completed')
        totalTasks.append({
            "task": task,
            "completed": completed,
            "username": employeeName,
        })

    updateUser = {user_id: totalTasks}
    file_json = f"{user_id}.json"

    with open(file_json, 'w') as f:
        json.dump(updateUser, f)
