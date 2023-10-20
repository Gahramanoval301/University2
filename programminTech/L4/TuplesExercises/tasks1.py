# Task1 : Sort reversely
tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)
list1.sort(reverse = True)
tuple1 = tuple(list1)
# print(tuple1)  
# ?-> Short form: tuple1 = tuple1[::-1]

# Task2 : Show 20
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple2[1][1])

#Task3 : Create single item in tuple:
tuple4=("Orange",)
# print(tuple4[0])

# Task4 : Unpack
tuple5 = (10, 20, 30, 40)
(a, b, c, d) = tuple5  #TODO It is possible that without ()
# print(a, b, c, d)

# Task5 : Swap tuples
tuple6 = (11, 22)
tuple7 = (99, 88)
tuple6, tuple7 = tuple7, tuple6
# print(tuple6, tuple7)

# Task6 : 44, 55 insert to another tuple
tuple8 = (11, 22, 33, 44, 55, 66)
tuple9  = tuple8[3:5]
# print(tuple9)

#Task7 : Modify Tuple
tuple10 = (11, [22, 33], 44, 55)
list10 = list(tuple10)
list10[1][0] = 222
tuple10 = tuple(list10)
# print(tuple10)

#Task8 : Sort Tuple (solve with lambda)
tuple11 = (('a', 23),('b', 37),('c', 11), ('d',29))
list11=list(tuple11)
list11.sort(key=lambda x: x[1])
tuple11 = tuple(list11)
# print(tuple11)

#Task10: Check the items are same ?
tuple12 = (20, 20, 20, 20)
if tuple12.count(20) == len(tuple12):
    print('True')





