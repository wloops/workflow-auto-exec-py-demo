import json
import os


folder_path = 'pre-step'
file_name = 'main_view_list.json'
file_path = os.path.join(folder_path, file_name)

with open(file_path, 'r') as f:
    data = json.load(f)

print(data)
