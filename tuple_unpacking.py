fruits = ("apple", "banana", "cherry","pawpaw","mango")
green, blue, *pink = fruits
print( pink)
print( green, blue)
green, _, _, _, _ = fruits
print(green)
thistuple = ("apple", "banana", "cherry")
for y in thistuple:
   print(y)

thistuple = ("apple", "banana", "cherry")
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
print ( crs_per_rab )
rabbits=(12)
print ( crs_per_rab )
# 5>9 and 5==8:
   ##print(true)
#5 < 3 or 5 == 5
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
name_length=len(given_name+""+middle_names+""+family_name)
print(name_length)
#trying format
print("Mohammed has {} balloons".format(27))
print("does your {} {} ".format("dog","bite"))
divine_string="divine loves {} and {} ".format("noodles","cake")
print(divine_string)
#split method
#my_str= "life is full of up and downs take life easy"
#my_str.split()
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
print(verse.find("and"))
print(verse.count("you"))
print(verse.rfind("you"))
#tuple
amaka=(345.6678,869.00)
print("amaka is at longtitude {}".format(amaka[1]))
location = (13.4125, 103.866667)
print("latitiude", location[0])
DIENSIONS=50,80,56
even,eve,odd=DIENSIONS
print('the numbers are {} {} {}'.format(even,eve,odd))
tuple_a = 6,8
tuple_b = (6,8)
print(tuple_a==tuple_b)
print(tuple_b[1])


 
# print(len(my_list))
#for i in range(len(thistuple)):
 # print(thistuple[i]))
print(not(5 < 3 and 5 == 5))

a = ['samuel', 'divine', 'james', 'vision']
print(a)

b = ': '.join(a) 
print(b)

c = '\n'.join(a)
print(c)

a.append('john')
print(a)
numbers = [1, 2, 6, 3, 1, 1, 6]
print(numbers)

a = 5

def changex():
   global a
   a = 7
   return "sam"

print(changex())
numbers = [1, 2, 6, 3, 1, 1, 6]
print(numbers)
unique_numbers=set(numbers)
print(unique_numbers)
fruit = {"apple", "banana", "orange", "grapefruit"} 
print("watermelon" in fruit)
months = {'January', 'Feburary', 'March'}
print(months)
print(months)
print(numbers.pop())
print(numbers)

wing1 = ["Divine", "Samuel", "Vision", "James"]
wing2 = ["Goodnews", "Mariam", "Sheriff"]

# staff_to_remove = wing1.pop()
# wing2.append(staff_to_remove)
wing2.append(wing1.pop())
print("Wing one staffs are: " + str(wing1))
print("Wing two staffs are: " + str(wing2))
print(wing2)

a = 1
print(type(a))
a = str(1)
print(type(a))
print(type(numbers))
numbers = set(numbers)
print(numbers)
print(type(numbers))
print(fruits)
print(fruit.pop())
numbers = [1, 2, 6, 3, 1, 1, 6]
b = numbers[2:5]
print(b)
numbers[6]
{"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}