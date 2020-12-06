import json

# json sample

userJson = '{"first": "max", "second": "essie", "adress":"121-todoni"}'

user = json.loads(userJson)

print(user['first'])

# dictionary to JSON
car = {'car': 'ford', 'make': 'mastang', 'model': 'cavara-s1'}

carJson = json.dumps(car)

print(carJson)