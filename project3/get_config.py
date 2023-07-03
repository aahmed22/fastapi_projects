import json 

with open('config.json') as file:
    file_contents = file.read()

config = json.loads(file_contents)