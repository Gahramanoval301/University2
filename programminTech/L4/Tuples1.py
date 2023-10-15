# A tuple is a collection which is ordered and unchangeable.Written in round brackets
# allow duplicate values
#Tuple items can be of any data type and contain:
# ! tuple() made tuples
# ! tuple with one element -> thistuple("apple",)->comma is required!
thistuple = ("pineapple", "banana", "cherry", "apple", "cherry")
print(len(thistuple), thistuple)
print(type(thistuple)) #<class 'tuple'>

# ? -------------------------Access Tuple Items-----------------------
print(thistuple[0], thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[-4:])
#* Check existences of items 
if "apple" in thistuple:
    print("'apple' exits in thistuple")
# ? -------------------------Change Tuple Items-----------------------
# Tuples are unchangeable, meaning that you cannot change, add,
#  or remove items once the tuple is created. But there are some workarounds.
#! You can convert the tuple into a list, change the list,
#!  and convert the list back into a tuple. 
newTuple = ('one', 'two', 'three', 'four', 'five')
newList = list(newTuple)
newList[-1] = 'six'
newTuple = tuple(newList)
print(newTuple)
# ! the second way of ADD ELEMENTS TO TUPLE:
newNumber =('eleven',)
newTuple += newNumber
print(newTuple)
#! remove items:   del keyword completely delete the tuple
newList.remove("four");
newTuple=tuple(newList)
print(newTuple)
#? -------------------------------Unpacking a tuple----------------------
dishes = ("pasta", "pizza", "hamburger", "doner" ,"sushi" )
(item1, item2, *items) = dishes
print(item1) #pasta
print(items) # ["hamburger", "doner" ,"sushi"]
(item1, *items, item2) = dishes
print(items) # ["pizza", "hamburger", "doner"]
#?-------------------------------Loop Through Tuples--------------------
animals = ("kitty", "dog", "cat", "oxen", "rabbit")
for animal in animals:
    print(animal)
#* Using the range() and len()
for i in range(len(animals)):
    print(animals[i])
#* Using while loop
animals = ("kitty", "dog", "cat", "oxen", "rabbit")
i = 0
while i < len(animals):
    print(animals[i])
    i += 1
#? -------------------------------Join Two Tuples--------------------
#* With + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2;
print(tuple3) #('a', 'b', 'c', 1, 2, 3)
#* Multiply Tuples
tuple3 = tuple1 * 2
print(tuple3) #('a', 'b', 'c', 'a', 'b', 'c')
#? ------------------------------Tuple Methods------------------------
#! count() and index()
animals = ("kitty", "dog", "cat", "oxen", "rabbit")
print(animals.count("kitty")) #1
print(animals.index("kitty")) #0

