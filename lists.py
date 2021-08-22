# create list
numbers = [1, 2, 3, 4, 5]
print(numbers)

fruits = ['apples', 'oranges', 'grapes', 'pears']

# get a value 
print(fruits[1])
'''
in javascript:
fruits.[0]
'''

# get length
print(len(fruits))
'''
in javascript:
console.log(fruits.length)
'''

# append to list 
fruits.append('Mangos')
'''
in javascript:
fuits.push('mangos')

'''

# remove from list
fruits.remove('grapes')

# insert into position
fruits.insert(2, 'strawberries')
'''
in javascript:
fruits[2]='strawberries '
'''

# remove with pop pop requirse an index
fruits.pop(2)

# reverse list order
fruits.reverse() 

# sort
fruits.sort()

# reverse sort
fruits.sort(reverse=False)
print(fruits)


# Slicing lists (this is accessing parts of a list)
languages = ['javascript', 'kotlin', 'go', 'python']

#get the first 3 languages remember: 
# while slicing the first element is inclusive
# and the last element is exclusive
languages_slice = languages[1:3]
print(languages_slice)

'''
in javascript:
      // The concept is the same inclusive exclusivity

      const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

      # The first two
      console.log(animals.slice(0,2)

      # The last three 
      console.log(animals.slice(2)
      console.log(-3)

      # The middle animal
      console.log(animals.slice(2,3)

'''


# Slicing from the beginning of the list
print(languages[:-1])

# chande th 2 and 3 element at a go
languages[1:3] = 'yellow' , 'orange'
print(languages)

# The four loop in python
for language in languages:
      print(language)

# append
languages.append('rust')

# insert
languages.insert('dart')

#copy 
languages.copy()

