
# functions 

def sayHello(name = 'sam'):
    print(f'hello {name}')

sayHello()

# return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(2,2)
print(num)

# labda function 
get = lambda num1, num2 : num1 + num2

print(get(4,3))