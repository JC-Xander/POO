import json

with open('persona.json', 'r') as file:
    data = json.load(file)

print(data['Persona']['Datos']['texto'])