#  classes

class User:
  # constractor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  def get_name(self):
    return print(f'my name is {self.name}')
# init User
max =  User('maxwel', 'max@email.com', '20')

max.get_name()

# In javascript
"""
  class User {
   // the difference is the constructor key word 
   //in python __init__ and use of self as compared to this in javascript 
   
    constructor(name, email, age) { 
      this.name = name
      this.email = email
      this.age = age
    }
    
    get_user_name() {
      console.log(`My name is ${this.name}`)
    }
  }
  
  //creating an instance of that class 
    const newUser = New User('james', 'james@email.com', 24)
    newUser.get_user_name()
  
"""


# extend class
class Customer(User):
    # constractor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

maxx = Customer('maxwel kiambati', 'max@email.com', 19)
maxx.set_balance(120000)
maxx.get_name()

# in javascript 
"""
class Car {
  constructor(brand) {
    this.carname = brand;
  }
  present() {
    return 'I have a ' + this.carname;
  }
}

class Model extends Car {
  constructor(brand, mod) {
    super(brand);
    this.model = mod;
  }
  show() {
    return this.present() + ', it is a ' + this.model;
  }
}

mycar = new Model("Ford", "Mustang");
document.getElementById("demo").innerHTML = mycar.show();
"""

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