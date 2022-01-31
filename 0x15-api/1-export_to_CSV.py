#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    file_name = "{}.csv".format(argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    request = "{}users/{}".format(url, argv[1])
    response_json = requests.get(request).json()
    name = response_json.get("name")
    task_res = requests.get("{}todos?userId={}".format(url, argv[1])).json()
    user_name = response_json.get("username")

    with open(file_name, mode='w') as csv_file:
        csvWriter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for info in task_res:
            csvWriter.writerow([argv[1], user_name,
                                info.get("completed"), info.get("title")])
