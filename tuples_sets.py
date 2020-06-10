#  an n tuple is an orderd collection. Allows duplicate numbers

# creating a tuple
fruits = ('apple', 'oranges', 'grapes')

# single element tuple should be trailled by a comma
fruits2 = ('cars',)

# get value 
# print(fruits[1])

# cant chage any value
# fruit(0) = 'almonds gives an error'

# delete the tuple
del fruits2

# print(fruits2) now gives an error with type 
# undefined because its already deleted

# get length
# print(len(fruits))


# a set is a collection which is unorderd and unidexed allows no duplicate numbers

# create a set
more_fruits_set = {'apples', 'oranges', 'mangos'}
fruits_set =  {'apples', 'onions', 'ngumus', 'carrots', 'oranges'}

# check if in set 
fruits_set.add('grapes')

# clear ser 
# fruits_set.clear()

# delete

# print(fruits_set)

# union
print(fruits_set.union(more_fruits_set))

# difference
print(fruits_set.difference(more_fruits_set))

# intersectrion 
print(fruits_set.intersection(more_fruits_set))