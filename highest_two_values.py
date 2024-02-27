items=[10,11,12,20,30, 20, 40]
items1 = [1]
items2 = []
items3 = [1,2,2,2,1]
items5 = [3,4]
items6 = [1, 1, 1]  
items7=[10,87,12,30,30, 70, 40, 85, 20, 48, 43,84]
items8=[34, 38, 98, 56, 73,55, 66, 68]
items9=[102,60,180,56,78,441,127,128 ]
def two_highest(arg1: list) -> list:
    #step 1 remove duplicates
    items = list(set(arg1))
    # print(items)
    #edges case; return item in descending order if length of item is less than or equals to 2
    if len(items) <= 2:
        # items.sort(reverse=True)
        return sorted(items, reverse=True) 
    #else: logic (example items [40, 10, 11, 12, 20, 30])
    result = items[:2] # [40, 10]
    # print(items)
    for item in items[2:]:
        for index, result_item in enumerate(result):
            if item > result_item:        
                if index == 0 and result[0] > result[1]:
                    result[1] = result[0]
                result[index] = item
                break
    return sorted(result, reverse=True)

def two_highest_v2(arg1):
    #step 1 remove duplicates
    items = list(set(arg1))
    # print(items)
    #step 2:edges case; return item in descending order if length of item is less than or equals to 2
    if len(items) <= 2:
        # items.sort(reverse=True)
        return sorted(items, reverse=True) 
    #else: logic (example items [40, 10, 11, 12, 20, 30])
    #step 3: [40, 30, 20, 12, 11]
    sorted_item = sorted(items, reverse=True)
    return sorted_item[:2]
# print(two_highest(items1))
# print(two_highest(items2))
# print(two_highest(items3))
# print(two_highest(items5))
# print(two_highest(items6))

# print(two_highest(items))
# print(two_highest(items7))
# print(two_highest(items8))
# print(two_highest(items9))
print(two_highest_v2(items1))
print(two_highest_v2(items2))
print(two_highest_v2(items3))
print(two_highest_v2(items5))
print(two_highest_v2(items6))

print(two_highest_v2(items))
print(two_highest_v2(items7))
print(two_highest_v2(items8))
print(two_highest_v2(items9))


# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []
# print(hand)
# while sum(hand)  < 17:
#     hand.append(card_deck.pop())
#     print(hand)