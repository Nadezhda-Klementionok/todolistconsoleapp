
Файл main.py описывает список дневных задач, каждая из которых описана параметрами 
- номер, наименование, приоритет, время выполнения с использованием json-server.

1. Назначение, краткое описание.

main.py - клиент-сервер- предназначен для формирования списка дневных задач в 
формате json/

2. Описание.

Программа работает в среде VS Code, базово с программой совместно работает файл day_tasks.json.

В исходном коде  используются следующие соглашения об импорте:
import requests
import json

Файл day_tasks.json содержит перечень задач(task), каждая из которых описана 4 параметрами:
- номер - id
- наименование - name
- приоритет - priority
- время выполнения задачи - time_to_spend

Программа содержит в себе следующие основные функции.

1 - show_json_and_dict() - Функция вывода содержимого файла day_tasks.json в виде json и словаря.
2 - task_get() - Функция вывода задач файла day_tasks.json, отсортированных по приоритету.
3 - task_get_id() - Функция вывода task по введенному id.
4 - task_delete() - Функция удаления task по введенному id.
5 - task_post() - Функция добавления нового task в day_tasks.
6 - task_put() - Функция изменения task в day_tasks.

Программа содержит функционал по выбору необходимой операции (функция main()):

3. Installation

3.1 git clone
3.2 setup node.js
	http://nodejs.org/en/download
3.3 install JSON server
	npm install -g json-server

4. Documentation

python -m pydoc .\main.py

5. Running the app

5.1 start JSON Server
	json-server --watch day_tasks.json
5.2 run the main app
	py main.py

6. Контактная информация.

Клементионок Надежда, kayat_n@tut.by

