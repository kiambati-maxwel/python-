# an example of a bird class
class Birds:
      def __init__(self, name, color, wingspan, sound):
            self.name = name
            self.color = color
            self.wingspan = wingspan
            self.sound = sound 
      def quack(self):
            print(f'hear me quack {self.sound}')
            
eagle = Birds('eagle', 'gray', 2, 'iiiieeeww iiiie!!!')

eagle.quack()

#an example of conditionals in python
first_number = 10
seconde_number= 23

if(first_number < seconde_number):
      print(f'{first_number} is greater than {seconde_number}')
else:
      print(f'{first_number} is less than {seconde_number}')

# Create a dictionary and delete the second element
my_dictionary = {'name': 'max', 'age': 21}

del(my_dictionary['name'])
print(my_dictionary)

# Convert into a string 
what_number = 33
print(str(what_number, type(what_number)))
#check type