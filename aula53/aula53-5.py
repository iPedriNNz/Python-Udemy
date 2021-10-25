import json

d1 = {
    'Pessoa1': {
        'nome': 'Pedro',
        'idade': 24,
    },
    'Pessoa2': {
        'nome': 'Amanda',
        'idade': 25,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)
