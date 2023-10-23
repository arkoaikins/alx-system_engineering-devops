# API :page_with_curl: 0x15. API
## In this project :bulb:
## Overview
- This is an API project where,
  - I acess employee data via an API to organize and export them to
    different data structures.
## Requirements of the project
- Used Vi/Vim editor
### Python Scripts
- files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- Code uses PEP 8 style(version 1.7)
- all modules have documention`(python3 -c 'print(__import__("my_module").__doc__)')`
- Code cannot be executed when imported(by using `if__name__=="__main__":)`

### Task 0
Python script that uses ths  [REST API](https://jsonplaceholder.typicode.com/) for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
- use `urllib` or `requests` module
- script must accept an integer as a parameter, which is the employee ID
- script must display on the standard output the employee TODO list progress in this exact
 - First line: Employee EMPLOYEE_NAME is done with
   tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
   - EMPLOYEE_NAME: name of the employee
   - NUMBER_OF_DONE_TASKS: number of completed tasks
   - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
 - Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
 Code is runned `python3 0-gather_data_from_an_API.py 2 
                 python3 0-gather_data_from_an_API.py 4
		 python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T"`