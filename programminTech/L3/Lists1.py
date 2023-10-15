
#Lists are used to store multiple items in a single variable.
#List items can be of any data type and contain
#List items are ordered, changeable, and allow duplicate values.
# ? -----------------------Create A List ---------------------------------------
thislist = ["apple", "banana", "cherry"]
thistuple =  ("apple", "banana", "cherry")
thisNewList = list(thistuple) #with list constructor
print(thislist, thisNewList)
#* type() ->(<class> 'list') and len()
# ? -----------------------Access Items ---------------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[0], fruits[-1]) 
#* range of indexes
print(fruits[:2]) #not include 2
#*Check if item exists in list
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
# ? -----------------------Change Items ---------------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1] = "blackcurrant"
print(fruits)
#* Changing range of item values
fruits[1:3] = ["strawberry", "watermelon"]
print(fruits)
#--------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1:2] = ["blackcurrant", "watermelon"] #change 1 item with 2 items
print(fruits) #indexes also will be change
# ? -----------------------Insert Items ---------------------------------------
#* insert() method
fruits = ["apple", "banana", "cherry", "orange"]
fruits.insert(1, ('apple2','apple3'))
print(fruits) 

#? ----------------------Append Items ----------------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
#* append() method
fruits.append("kiwi")
print(fruits)
#*Extend a list: extend() method (any iterable object)
fruits.extend(("pineapple", "mango"))
print(fruits)
#? -----------------------Remove Items ---------------------------------------
#* remove() method
fruits = ["apple", "banana", "cherry", "orange", "banana"]
fruits.remove("banana")  #removes the first occurrence of
print(fruits)
#* pop() method -> remove last item or specified index
fruits = ["apple", "banana", "cherry", "orange", "banana"]
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
#* The del keyword can also delete the list completely.
#* clear() method -> list will be empty -> []
#? -----------------------Loop List Items --------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit)
#* using len() and range() -> with indexes
for i in range(len(fruits)):
    print(fruits[i])
#* using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
#* using list comprehension

fruits = ["apple", "banana", "cherry", "orange"]
[print(fruit) for fruit in fruits]
#The Syntax -> Do this for this collection in this situation

#? -----------------------Sort List Items --------------------------------
fruits = ["apple", "banana", "pineapple", "orange"]
fruits.sort()
print(fruits)
#* Sort descending order: 
fruits.sort(reverse=True)
print(fruits) #['pineapple', 'orange', 'banana', 'apple']
#*Customize Sort Function -> key = function

fruits = ["apple", "pie", "pineapple", "orange"]
fruits.sort(key=len)
print(fruits) #['pie', 'apple', 'orange', 'pineapple']
#---------------other example:
def sort(n):
    return abs(n-50)
numbers = [51,46, 102,32, 13, 5, 2, 12]
numbers.sort(key=sort)
print(numbers) #[51, 46, 32, 13, 12, 5, 2, 102]
#* Case Insensitive Sort!!!!!!!!!! -> key=str.lower()
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key = str.lower)
print(fruits)
#TODO we have also reverse() function
#? -----------------------Copy List Items --------------------------------
#! You cannot copy a list simply by typing list2 = list1 (reference problem)
#* Using copy() or list()  methods:
fruits = ["apple", "banana", "cherry"]
myFruits = thislist.copy()
print(myFruits)  
#? -----------------------Join Two Lists --------------------------------
#* 1.using + operator:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
#* appending all the items from list2 into list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for list in list2:
    list1.append(list)
print(list1) #['a', 'b', 'c', 1, 2, 3]
#* you can use also extend() method -> list1.extend(list2) -> print(lis1)
# ? ----------------------------index() and count() methods:

fruits = ["apple", "banana", "cherry", "orange"]
print(fruits.index("orange")) #3
print(fruits.count("orange")) #1

#! ADVANCED
#? ----------------------------List Comprehension:---------------------
#•	List comprehension offers a shorter syntax when you want to create a new list
#  based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for fruit in fruits:
  if "a" in fruit:	
    newlist.append(fruit)
print(newlist)
#* do This with list comprehension in one line:
#TODO The Syntax -> Do this for this collection in this situation
fruits = ['apple', 'cherry', 'strawberry', 'orange']
newlist = [print(fruit) for fruit in fruits if "a" in fruit ]
print(newlist)
#! The condition is optional and can be omitted:
#* you can use it with range() method
#Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [fruit.upper() for fruit in fruits]
print(newlist)
