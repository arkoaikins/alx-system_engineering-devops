#!/usr/bin/python3
"""
Script that uses REST API to return information about an
employee's TODO list progress
"""
import json
import sys
from requests import Session

if __name__ == "__main__":

    s = Session()
    # counter for completed tasks
    task_done = 0
    # URL's to get employee's tasks and name
    user_id = sys.argv[1]
    emp_tasks = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)
    emp_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # HTTP requests to the API via the URLS to get employee tasks and name
    # and parsing the JSON response
    employee_todo = (s.get(emp_tasks)).json()
    employeeName = (s.get(emp_name)).json()['name']

    # check total tasks and count completed tasks
    for progress in employee_todo:
        if progress['completed']:
            task_done = task_done + 1
    # print the progress
    print("Employee {} is done with tasks({}/{}):".
          format(employeeName, task_done, len(employee_todo)))

    # listing the titles of tasks that have been completed
    for progress in employee_todo:
        if progress['completed']:
            print("\t " + progress.get('title'))
