def my_function(greeting):
    print(greeting  + " hello ")
my_function( "kedu" )

def my_function3(fname):
  print(fname + " Refsnes")
my_function3("Emil")
my_function3("Tobias")
my_function3("Linus")

def good_fruits(*fruits):
   print("the best fruit is" + fruits[4])
good_fruits("pawpaw","orange","mango","pear"," tomatoes ")

def my_function(food):#different
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def area_of_square(L):
   return L*L
print(area_of_square(5))

class MyClass:
  x = 5

print(MyClass)

