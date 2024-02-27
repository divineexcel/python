class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = student("John", 36)

# print(p1.name)
# print(p1.age)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
print(a[3])
a.append(56)
print(a)

str1 = "Udacity"
str3 = "Welcome, Constance!"
marks = 100
print(str3 +  "you scored"  +  str ( marks))
x = "awesome"

def myfunc():
  global x 
  x= "away"
  print("Python is " + x)

myfunc()

print("Python is " + x)
y = str(2.8)
print (type(y))
import random

print(random.randrange(1, 10))
txt = "The best things in life are free!"
print("go" in txt)
if "go" in txt:
  print("Yes, 'free' is present.")
else:
  print("nothing")
  a = "Hello World"
print(a.split())


class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age


class Product:
  def __init__(self, product_name: str, price: float, quality: str):
    self.name = product_name
    self.price = price
    self.quality = quality


employee1 =  Employee("Samuel", 3)
employee2 =  Employee("Divine", 5)

print(employee1.age)

product1 = Product('Canvas Shoe', 2000.00, 'High')
product1 = Product('Canvas Shoe', 2000.00, 'Low')
product1 = Product('iPhone 14', 2000.00, 'High')







