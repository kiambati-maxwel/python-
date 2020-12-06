# open file
my_file = open('test.txt', 'w')

# info
print(my_file.name)
print(my_file.closed)
print(my_file.mode)

# write to file
my_file.write('im stsrting to feel python')
my_file.close()

# append to file 
myfile = open('test.txt', 'a')
myfile.write('and Typescript')
myfile.close()

# read from file
my_file = open('test.txt', 'r+')
text = my_file.read(100)
print(text)