# a dictionary is a collection which is unorderd, chageable and indexed, no Duplicate members.

# create dict
person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}

print(person, type(person))

# in javascript
"""
const myobj = {
    first_name: 'john',
    second_name: 'doe',
    age: 30
    }

console.log(myobj.age)
"""

# get value
print(person['first_name'])
print(person.get['last_name'])
# in javascript:
"""
console.log(person.fistname)
"""

# add key/value
person['phone'] = '+2547 227 890'

# get dict keys 
print(person.keys())
"""
in javascript: object.getOwnPropertyNames(myobj) to get all the keys
Object.values

"""

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'BOston'

# remove item
del (person['age'])
""" 
javascript :
    delete myobject.key
"""
 
#  get length
print(len(person2))

# list of dict

people = [
    {'name': 'martha', 'age' :30},
    {'name': 'kelvin', 'age' :25 }
]

print(people[1]['name'])

'''
In Javascrip: 
An object in javascript can not allow duplicate keys.
'''

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

print("carbon" in elements)
print(elements.get("dilithium"))

n = elements.get("dilithium")
print(n is None)
print(n is not None)