#concantenate
# name = 'john'
# age = 24

# print('my name is ' + name )

# # argument by position String formating 

# print('my name is {name}  i am {age} yrs old'.format(name = name, age = age))

# # f strings (3.6 + )

# print(f'my name is {name} and i am {age} yrs')

s = 'hello world'

# a banch of string methods

# capitalize string
print(s.capitalize())

# make all to upper case
print(s.upper())
 
# swap case
print(s.swapcase())

# get length 
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# count
sub = 'h'
print(s.count(sub))

# starts with
print(s.startswith('hello'))

# ends with
print(s.endswith('d'))

# split into list
print(s.split())

#find position
print(s.find('r'))

# is all alphanumerical 
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric 
print(s.isnumeric())

#input text 
first_name = input('please input your first name: ')
second_name = input('please input your second name: ')

print(f'hello {first_name.capitalize()} {second_name.capitalize()}. Hae are you doing mahn ?')
'''
In JavaScript:
const name = prompt(what is your name ?);
console.log(name);
'''

#convert to string
days_in_feb = 28
print(str(days_in_feb) + ' days in february')
'''
#in javascript:
      const days_in_feb = 28
      console.log(days_in_feb.toString())
      String(days_in_feb)
'''

#convert from string to int all float
first_num = input('enter first num: ')
second_num = input('enter second number: ')
print(f'input always takes in a string {first_num} + {second_num} = {int(first_num) + float(second_num)}')

'''
in javascript:
to number : Number("3.44")

Converting Dates to numbers:
d = new Date()
Number(d)

or 

d = new Date()
d.getTime()
'''