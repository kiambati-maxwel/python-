# Write a program that Manipulate only one bit in an octal, 
# value using bitwise operators (the 4th bit)

# First, how do you print octol values (0o) notation
octal_value = 0o67
print(bin(octal_value))

# Check the state of the fourth value
# Remember values begin from 0 so the fourth value is actually the fifth bit
# Now to check the fifth bit you can perform a conjuction with only the fifth bit a 1
# if the fifth bit is one then it looks something like this 00010000 which in decimal is 16 so if you 
# check the conjnciton of your actal value with a bit mask of 16
print(bin(16))
print(bin(octal_value & 16))

# so simply
if octal_value & 16:
    print('Bit is set')
else:
    print('bit is not set bro')



# Challange 2, simulate how sub-net mask work in IPv4