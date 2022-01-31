#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    request = "{}users/{}".format(url, argv[1])
    response_json = requests.get(request).json()
    name = response_json.get("name")
    task_response = requests.get("{}todos?userId={}".format(url, argv[1])).json()
    num_task = len(task_response)
    completed_tasks = requests.get("{}todos?userId={}&&completed=true"
                                  .format(url, argv[1])).json()
    num_completed_task = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, num_completed_task, num_task))
    for index in completed_tasks:
        task_title = index.get("title")
        print("\t " + task_title)
