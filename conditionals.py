x = 10 
y = 50

#comparison operators (==, !+, > < )
''' 
In javascript: === !== 
'''

# if

if x > y:
   print(f'{x} is greater than {y}')

# if else

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} equals than {y}')
else:
    print(f'{y} is less  than {x}')

# logical operators and or not
if x > 2 and x <= 10:
    print(f'{x} is greater to 10')

if not(x == y):
    print('something')

# membership in not in
numbers = [1, 2, 3, 4, 5]

if 2 in numbers:
    print('its in numbers')

if 10 not in numbers:
    print('not in numbers')


# ar statement 
if 2 == 3 or 4 == 5:
    print('theres no math')
else:
    print('did we not agree math is not real')

''' 
 In JavaScript:
    if(2===3 || 4===5){
        // do something...
    }else (){
       // do something...
    }
'''


# in statement for lists

myList = ['ontorio', 'paris', 'singerpore']
if 'ontorio' in myList:
    print('tax is 12.33')

'''
In JavaScript:
    check if an element exists in an array
    array.indexOf(element) > 0
    or includes(element) // slower than index of but checks 
                         // if you have passed a regExp and throughs an
                         // exeption
'''

fruits = ['oranges', 'mangoes', 'watermelones', 'pineapples', 'apples', 'avocados',  'ostritches']

if('oranges', 'apples' in fruits):
    fruits.remove('oranges') 
    fruits[fruits.index('apples')] = 'onions'
    print(fruits)
else:
    print('there are no oranges and apples in the list')