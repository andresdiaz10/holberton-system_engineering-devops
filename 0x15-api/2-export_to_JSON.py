#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    file_name = "{}.json".format(argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    request = "{}users/{}".format(url, argv[1])
    response_json = requests.get(request).json()
    name = response_json.get("name")
    task_res = requests.get("{}todos?userId={}".format(url, argv[1])).json()
    user_name = response_json.get("username")
    todo_dict = {}
    todo_list = []
    for index in task_res:
        tasks = {}
        tasks["task"] = index.get('title')
        tasks["completed"] = index.get('completed')
        tasks["username"] = response_json.get('username')
        todo_list.append(tasks)
    todo_dict[int(argv[1])] = todo_list
    with open(file_name, mode='w') as json_file:
        json.dump(todo_dict, json_file)
