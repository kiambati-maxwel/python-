# #  classes

# class User:
#   # constractor
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
#   def get_name(self):
#     return print(f'my name is {self.name}')
# # init User
# max =  User('maxwel', 'max@email.com', '20')

# max.get_name()


# # extend class
# class Customer(User):
#     # constractor
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
#     self.balance = 0

#   def set_balance(self, balance):
#     self.balance = balance

# maxx = Customer('maxwel kiambati', 'max@email.com', 19)
# maxx.set_balance(120000)
# maxx.get_name()

class myName:
  def __init__(self):
    self.name = 'max'
  def getName(self):
    print(self.name)

max = myName()

max.getName()

class newName(myName):
  def __init__(self):
    self.name = 'essie'

essie = newName()
essie.getName()

print(newName)