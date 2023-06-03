
���� main.py ��������� ������ ������� �����, ������ �� ������� ������� ����������� 
- �����, ������������, ���������, ����� ���������� � �������������� json-server.

1. ����������, ������� ��������.

main.py - ������-������- ������������ ��� ������������ ������ ������� ����� � 
������� json/

2. ��������.

��������� �������� � ����� VS Code, ������ � ���������� ��������� �������� ���� day_tasks.json.

� �������� ����  ������������ ��������� ���������� �� �������:
import requests
import json

���� day_tasks.json �������� �������� �����(task), ������ �� ������� ������� 4 �����������:
- ����� - id
- ������������ - name
- ��������� - priority
- ����� ���������� ������ - time_to_spend

��������� �������� � ���� ��������� �������� �������.

1 - show_json_and_dict() - ������� ������ ����������� ����� day_tasks.json � ���� json � �������.
2 - task_get() - ������� ������ ����� ����� day_tasks.json, ��������������� �� ����������.
3 - task_get_id() - ������� ������ task �� ���������� id.
4 - task_delete() - ������� �������� task �� ���������� id.
5 - task_post() - ������� ���������� ������ task � day_tasks.
6 - task_put() - ������� ��������� task � day_tasks.

��������� �������� ���������� �� ������ ����������� �������� (������� main()):

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

6. ���������� ����������.

������������ �������, kayat_n@tut.by

