# my_list = [(22,), (2,), (3,), (4,), (5,)]
# my_list = [(0, 1), (22,89), (2,65), (3,7), (4,8),(8, 5)]
my_list = [('Samuel', 67),('mike',32),('div',67),('him',56),('girl',53),('game',90)]
#for  name, position in my_list:
for index, value in enumerate(my_list):
    print(value)
    name, position = value

    #print( str(index) + '. ' + str(name) + ' took ' + str(position) + ' position ')
    # print(index)
    

# {index}. {name} took {position} position
# 1. Samuel took 67 position
# 2. mike took 32 position



# for item, index in my_list:
#     print('The value of item is: ' + str(index))
#     print('yes')
# print('end')
# for g, value in enumerate(my_list):
#     print('The index value is: ' + str(g) + '. The value at i is: ' + str(value))

# The index value is {index}. The value at i is {value}
first_value, second_value, third_value = (3,4,5)

# print(first_value)
#set
a=[1,2,2,3,3,3,4,4,4,4]
b=set(a)
print(b)
print(len(a)-len(b))
b.add(5)
b.pop()
print(b)
#dic
elements={"hydrogen":1,"carbon":6,"helium":2}
elements["oxygen"]=4
print(elements)
print(elements.get("icro"))
print("micro"in elements)
n = elements.get("dilithium")
print(n is None)
print(n is not None)
population={"Shanghai":17.8,"Istanbul":13.3,"Karachi":13.0,"Mumbai":12.5}
print(population)
#compound
elements2={"hydrogen":
           {"weigth":1.00794,
            "symbol": "H"},
            "helium":
            {"weight":4.002602,
             "symbol":"c"}}
#helium = elements
#print(helium
#conditional stateents
phone_balance=3
bank_balance=100
print(phone_balance, bank_balance)
if phone_balance<5:
    phone_balance+=10
    bank_balance-=10
print(phone_balance,bank_balance)
n=6
if n % 2==3:
    print(f"number {n}  even")
else:
    print(f"number {n} odd")
season="rainny"
if season=="winter":
   print("water the garden")
elif season=="summer":
  print("plant the garden")
elif season=="rainny":
    print("stay in doors")
else:
    print("unrecognized season")

age=30
if age<=20:
    print("computer science")
elif age<=30:
    print("biology")
elif age==50:
    print("maths")
else:
    print("no course")
message="someone who is {} can study {}".format(age,"biology")
age = 36
txt = "My name is John, and I am {}".format(age)
print(txt)
print(message)
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(cities)
names=["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
username=[]
for name in names:
    name=name.lower().replace(" ","_")
    print(name)
    username.append(name)
print(username)


def addition(a, b):
    return a + b


print(addition(55, 54))
print(addition(54, 64))
print(addition(65, 64))
print(addition(65, 54))
print(addition(545, 5334))
print(addition(4355, 54))
print(addition(5335, 54))


print('==============================')
print(322 + 32)
print(323 + 3443)
print(322 + 32)
print(32333 * 34233)
print(3232 * 32)
print(323 * 3443)
print(3322 * 32)
print(33323 * 3443)



   
    