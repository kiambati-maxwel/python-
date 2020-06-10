# a dictionary is a collection which is unorderd, chageable and indexed, no Duplicate members.

# create dict
person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}

print(person, type(person))

# get value
print(person['first_name'])
# print(person.get['last_name'])

# add key/value
person['phone'] = '+2547 227 890'

# get dict keys 
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'BOston'

# remove item
del (person['age'])
 
#  get length
print(len(person2))

# list of dict

people = [
    {'name': 'martha', 'age' :30},
    {'name': 'kelvin', 'age' :25 }
]

print(people[1]['name'])


elements = {"hydrogen": 1, "helium": 2, "carbon": 6}


print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary


print("carbon" in elements)
print(elements.get("dilithium"))

n = elements.get("dilithium")
print(n is None)
print(n is not None)