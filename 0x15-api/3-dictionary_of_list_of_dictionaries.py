#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress."""

import json
import requests

if __name__ == "__main__":
    file_name = "todo_all_employees.json"
    url = 'https://jsonplaceholder.typicode.com/'
    response_user = requests.get("{}users".format(url)).json()
    response_task = requests.get("{}todos".format(url)).json()
    todo_dict = {}
    user_dict = {}
    for index in response_user:
        user_id = index.get('id')
        todo_dict[user_id] = []
        user_dict[user_id] = index.get('username')
    for index in response_task:
        tasks_all_emp = {}
        user_id = index.get('userId')
        tasks_all_emp["task"] = index.get('title')
        tasks_all_emp["completed"] = index.get('completed')
        tasks_all_emp["username"] = user_dict.get(user_id)
        todo_dict.get(user_id).append(tasks_all_emp)
    with open(file_name, mode='w') as json_file:
        json.dump(todo_dict, json_file)