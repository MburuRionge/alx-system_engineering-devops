#!/usr/bin/python3
'''
Exports all data to JSON
'''
import json, requests, sys
from collections import OrderedDict


def get_users_todo():

    emp = requests.get('https://jsonplaceholder.typicode.com/users')
    users = {}
    final_id = OrderedDict()
    filename = "todo_all_employees.json"

    for item in emp.json():
        users[item['id']] = item['username']

    with open(filename, 'w+') as f:
        for user in users:
            tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(user))
            tasks = tasks.json()
            res = []
            for task in tasks:
                final = OrderedDict()
                final['username'] = users[user]
                final['task'] = task['title']
                final['completed'] = task['completed']
                res.append(final)
            final_id[user] = res
        json.dump(final_id, f)


if __name__ == "__main__":
    get_users_todo()
