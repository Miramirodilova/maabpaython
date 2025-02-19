import json
import os
import requests

columns = 'id,name,birth_year,death_year,nationality\n'
with open('actors.json', 'r') as f:
    data = json.load(f)
for i in data:
    id = i['id']
    name = i['name']
    birth_year = i['birth_year']
    death_year = i.get('death_year', 'no info')
    nationality = i['nationality']
    actor_image = i['image']
    folder_path = f'Project\{name}'
    csv_file_path = f'{folder_path}\{name}.csv'
    jpeg_file_path = f'{folder_path}\{name}.jpeg'
    os.makedirs(folder_path, exist_ok=True)
    with open(csv_file_path, 'w') as f:
        f.write(columns)
        values = f'{id},{name},{birth_year},{death_year},{nationality}'
        f.write(values)
    with open(jpeg_file_path, 'wb') as f:
        response = requests.get(actor_image)
        f.write(response.content)
