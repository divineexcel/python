population=500
population+=500
print(population)
print(4%3)
print(2%15)
print(str(567))
print(type(567))
n=4
if  n == 1 :
     print ("Weird")
elif n == 2 and range  (2 , 5):
     print ("Not Weird")
     
elif n >= 2 and  range (6 , 20):
     print ("Weird")
elif n == 4 > 20:
    print ("Not Weird")
else:
     print("nothing")
months=["april","may","june"]
print("sunday"in months)
print("may" in months)
age = 14
is_teen = age > 12 and age < 20
print(is_teen) 
money=10000
is_rich = money > 1000 and money < 100000
print(is_rich)
first_word="hello"
print(first_word *5 )
errors = 0
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
points=150
result="none"
if points <= 50:
    result= "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result="Oh dear, no prize this time."
elif points <= 180:
    result= "Congratulations! You won a wafer-thin mint!"
else:
    result= "Congratulations! You won a penguin!"
if result:
    print(result)
else:
    print("Oh dear, no prize this time.")
cities=["aba", "abuja","lagos"]
for h in cities:
    print(h.title())
    cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    print(capitalized_cities)
cities = ['ghy', 'mountain ', 'ccago', 'los']

for l in range(len(cities)):
    cities[l] = cities[l].title()
    print(l)
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for g in range(len(usernames)):
    usernames[g]=usernames[g].replace(" ","_")
    print(usernames)
items=["frist tag","second tag"]
htmlstr="url/n"
for item in items:
    item ="<li>" + item +"</li" +"</ui>"
    htmlstr+=item
    print(item)
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
counter={}
for word in book_title:
    #
    #print(word)
    if word not in counter:
        counter[word]=8
    else:
        counter[word]+=1
        #print(counter)
        for word in book_title:
            # print(counter)
            # if word == 'gasby':
            #     print(counter.get(word)
            counter[word]=counter.get(word,0)+1
            print(counter)
print(counter)
# s=["abab"]  
# print(s.index("b"))
arr = [3,43,4,43,3]
# def double(number):
#     return number * 2
# print(list(map(double, arr)))
#using lambda
print(list(map(lambda x: x * 2, arr)))


# def square(number):
#     return number ** 2
# print(list(map(square, arr)))
# using lambda
# print(list(map(square, arr)))
print(list(map(lambda y: y **2,  arr)))


print(list(filter(lambda y: y > 10,  arr)))

