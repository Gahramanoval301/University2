print (0X20) #1
a = 20; #int
b = 'Hello World' #string
c = True #bool
d = 2E34 #float 
e = 2. #float
print(type(a), type(b), type(c), type(d), type(e));

print('a\
....b')  #! \- bu boslugu saymamaga icaze verir 
print('a \n b') #! \n - nextline 

#todo Lists 
list1 = [1, 2, 3, 'A', 'b', ["salam", 2]]
print(list1) #TODO fist print for lists in python

x=list(); #* List is used for take variables and order in list (square brackets)
print(x);

list2 = (1, 23, 'A', True);
print(list(list2))

#Unpack lists
fruits = ['apple', 'orange', 'banana']
friut1, friut2, friut3 = fruits; #* this is called desctructing in js
print(friut1, friut2, friut3)

#TODO Multiple Assignment 
var1, var2, var3 = 1, True, 'salam';
print(var1, var2, var3);

#TODO combine text and a variable 
x  = 'awesome'
y= 'Python is'
# print('Python is ' + x) #!CONCENETATION
print(y , x) #!CONCENETATION //y+x//y + ' ' + x

#Todo Conditional Expressions

con = 'T' if True else 'false'
print(con)

#Todo Generator Expressions
gen= (i for i in 'cbf')
print(gen)

#Todo Casting: 
print(bool(3))

#todo Import Random
import random;
print(random.randrange(1, 5)) #for random numbers

#Todo booleans
print(bool(0))  #False
print(bool({}))   #False
print(bool('salam23'))  #True
print(7>2)  #True

print('leman'*2); # output: lemanleman
print('leman' + 5) #! throw an error!!!!!!!!!!

