items = [34,26,78,35,21,11,64,88,72,89,58, 60,75]
# new_items = []
# for i in items:
#     if i % 2 != 0:
#         break
#     new_items.append(i)
# # 34,26,78,64,88,72,58,60
# print(new_items)
items = [(34,26),(78,35),(21,11),(64,88),(72,89),(58,60)]
greater_vale =[]
for first_item, second_item in items:

    #print(first_item)
    if first_item > second_item:
        greater_vale.append(first_item)
    else :
        greater_vale.append(second_item)
        
    
print(greater_vale)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [ name.split()[1].lower() for name in enumerate(names)]
print(first_names)
    

        




#new_items = [item for item in items if item % 2 == 0]
#print(new_items)