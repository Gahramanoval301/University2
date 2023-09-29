# lists
list = [1, 2, 3, 4, 'Salam']
print(list[0:4])
list.append(7)
print(list)
print(list.insert(2, 'Salam2'))  # ! NONE
print(list)
# list.remove(9)  # ! 9 not in list
# also with removee ->.pop(), del list[1]
# list.clear()
# print(list)
list[1:3] = ["watermelon"]
print(list)
print(1 in list)  # True
print(len(list))  # list.length in JS
if "watermelon" in list:
    print('I love watermelon!')
else:
    print('NOOOO')
for item in list:
    print(item)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # also tuples and sets
print(thislist)
# tuples

tuple1 = (1, 2, 34, 2, 34, 2)
print(tuple1.count(34))  # 2 occurences
