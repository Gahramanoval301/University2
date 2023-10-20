# Task1 : sort reversely
list1 = [100, 200, 300, 400, 500]
list1.sort(reverse=True)
# print(list1)

# Task2 join to lists to lists
list2 = ["M", "na", "i", "Ke"]
list3 = ["y", "me", "s", "lly"]

newList = []
for i in range(len(list2)):
     newList.append(list2[i] + list3[i])    
# print(newList)

#Task3 : Find exponent of numbers in list
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
# print(numbers)

#Task4: Mixed lists
list4 = ["Hello ", "take "]
list5 = ["Dear", "Sir"]
newList2 = []
for i in range(len(list4)):
    for j in range(len(list5)):
        newList2.append(list4[i] + list5[j])
# print(newList2)

#Task6: Remove empty strings
list6 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for word in list6:
    if word == "":
        list6.remove(word)
# print(list6)

# Task7 : Add 7000 to complex array
list7 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list7[2][2].append(7000)
# print(list7)

#Task8 : Replace 200 to 20
list8 = [5, 10, 15, 20, 25, 50, 20]
list8[list8.index(20)] = 200
# print(list8)

#Task9
list9 = [5, 20, 15, 20, 25, 50, 20, 12, 20, 20]
for number in list9:
    if list9.count(number) > 1:
        list9.remove(number)
print(list9)
# while 20 in list1:
#     list1.remove(20)
# print(list1)