# Write a program that Manipulate only one bit in an octal, 
# value using bitwise operators (the 4th bit)

# First, how do you print octol values (0o) notati
octal_value = 27
octal_mask = 16

# Check the state of the fourth value
# Remember values begin from 0 so the fourth value is actually the fifth bit
# Now to check the fifth bit you can perform a conjuction with only the fifth bit a 1
# if the fifth bit is one then it looks something like this 00010000 which in decimal is 16 so if you 
# check the conjnciton of your actal value with a bit mask of 16

print(bin(octal_value))
print(bin(octal_mask))

# so simply
if octal_value & octal_mask:
    print('Bit is set ')
    
    # This is how you reset the bit to 0
    octal_value &= ~octal_mask
    print(bin(octal_value))
else:
    print('bit is not set bro')

    octal_value |= octal_mask
    print(bin(octal_value)) 
    print(octal_value)
 
 # flat out negate the sigle bit (make it act like a switch )

def flip_5th_bit (octal_value):
    # Xor
    octal_value ^= octal_mask
    print(f'{bin(octal_value)}: {octal_value}')

flip_5th_bit(octal_value)


# Binary shifting
number = 10
shift_left = number << 1 # number * 2 raised to power 1
shift_right = number >> 2 # floor => number / 2 raised to the power of 2

print(number, shift_left, shift_right)


# Challange 2, simulate how sub-net mask work in IPv4