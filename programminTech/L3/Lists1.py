
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
