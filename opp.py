
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)
add_numbers(8,10)
def find_square(num):
    result = num * num
    return result
import math
# sqrt computes the square root
square_root = math.sqrt(4)
print("square eauales:", square_root)
# pow() comptes the power
power = pow(2, 3)
print("2 to the power 3 is",power)
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()
#classes

se1=["software engineer", "Dan", 19, 5000]
se2=["software engineer", "Lisa", 23, 8000]
def code(de):
    print(f"{de[1]} is wring xode........")
code(se1)
class softwareengineer:
   def __init__(self,name,age,salary):
       self.name=name
       self.age=age
       self.salary=salary
   def codee(self):
       print(f"{self.name} is writing codes.....")

   def code_language_():
       pass
   
   
see1= softwareengineer("Dan", 19, 5000)
print(see1.age)

see1.codee()