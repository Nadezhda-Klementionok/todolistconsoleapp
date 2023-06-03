import requests
import json

key_names = ['id', 'task', 'priority', 'time_to_spend']
key_widths = [10, 18, 10, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_tasks(task):
    for (n, w) in zip(key_names, key_widths):
        print(str(task[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for task in json:
            show_tasks(task)
    elif type(json) is dict:
        show_tasks(json)
    else:
        show_empty()


def show_json_and_dict():
    '''Функция вывода содержимого файла day_tasks.json в виде json и словаря.'''
    try:
        reply = requests.get("http://localhost:3000/day_tasks")
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            print('json: ', reply.text)
            print('dict:', reply.json())
        else:
            print('Server error')


def task_get():
    '''Функция вывода задач файла day_tasks.json, отсортированных по приоритету.'''
    try:
        reply = requests.get(
            "http://localhost:3000/day_tasks?_sort=priority&_order=desc")
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        else:
            print('Server error')


def task_get_id():
    '''Функция вывода task по введенному id.'''
    id = input('Enter id: ')
    try:
        reply = requests.get(f'http://localhost:3000/day_tasks/{id}')
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:
            print('Resource not found')
        else:
            print('Server error')


def task_delete():
    '''Функция удаления task по введенному id.'''
    id = input('Enter id to delete: ')
    try:
        reply = requests.delete(f'http://localhost:3000/day_tasks/{id}')
        reply = requests.get(
            "http://localhost:3000/day_tasks?_sort=priority&_order=desc")
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:
            print('Resource not found')
        else:
            print('Server error')


def task_post():
    '''Функция добавления нового task в day_tasks.'''

    h_close = {'Connection': "Close"}
    h_content = {'Content-Type': 'application/json'}
    new_task = {
        'id': 6,
        'task': 'english_learning',
        'priority': '4',
        'time_to_spend': 20
    }
    print(f'New task: {json.dumps(new_task)}')

    try:
        reply = requests.post(f'http://localhost:3000/day_tasks', headers=h_content,
                              data=json.dumps(new_task))
        reply = requests.get("http://localhost:3000/day_tasks")
        reply = requests.get(
            f'http://localhost:3000/day_tasks/', headers=h_close)
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:
            print('Resource not found')
        else:
            print('Server error')


def task_put():
    '''Функция изменения task в day_tasks.'''

    h_close = {'Connection': "Close"}
    h_content = {'Content-Type': 'application/json'}

    id_change = input('Enter id to change: ')
    task_change = input('Enter task to change: ')
    priority_change = input('Enter priority to change: ')
    time_to_spend_change = input('Enter time_to_spend to change: ')

    tasks_change = {
        "id": id_change,
        "task": task_change,
        "priority": priority_change,
        "time_to_spend": time_to_spend_change
    }

    try:
        reply = requests.put(f'http://localhost:3000/day_tasks/{id_change}', headers=h_content,
                             data=json.dumps(tasks_change))
        reply = requests.get("http://localhost:3000/day_tasks")
        reply = requests.get(
            f'http://localhost:3000/day_tasks/', headers=h_close)
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:
            print('Resource not found')
        else:
            print('Server error')


def main():
    '''Функция ввода номера, имени, приоритета и времени выпролнения задач на день.'''
    print('Возможные операции:')
    print(f'1 - {show_json_and_dict.__doc__}')
    print(f'2 - {task_get.__doc__}')
    print(f'3 - {task_get_id.__doc__}')
    print(f'4 - {task_delete.__doc__}')
    print(f'5 - {task_post.__doc__}')
    print(f'6 - {task_put.__doc__}')
    print(f'0 - Exit')

    put = int(input('Enter operation number: 1 - 6 or 0 to exit:'))

    while put != 0:

        if put == 1:
            show_json_and_dict()
        elif put == 2:
            task_get()
        elif put == 3:
            task_get_id()
        elif put == 4:
            task_delete()
        elif put == 5:
            task_post()
        elif put == 6:
            task_put()
        else:
            print('Bad operation!')

        put = int(input('Enter operation number: 1 - 6 or 0 to exit:'))


if __name__ == "__main__":
    print('Main.py запущена самостоятельно.')
    main()
else:
    print('Main.py импортирована.')
