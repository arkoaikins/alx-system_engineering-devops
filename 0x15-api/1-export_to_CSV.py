#!/usr/bin/python3
"""
Extention of task 0 script to export data in CSV format
"""
import csv
import json
from requests import Session
import sys

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

    # export data is CSV format
    csv_file = user_id + '.csv'

    with open(csv_file, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in employee_todo:
            completed = todo.get('completed')
            title = todo.get('title')
            write.writerow([user_id, employeeName, completed, title])
