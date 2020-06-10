x = 10 
y = 50

#comparison operators (==, !+, > < )

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







