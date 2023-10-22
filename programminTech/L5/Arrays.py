array1 = ['apple', 'banana', 'cherry', 'avakado']
array1[0] #apple
array1[0] = 'pineapple' #modify the apple with banana
print(array1) #['banana', 'banana', 'cherry', 'avakado']
print(array1.index('banana'))
# ?----------------------->Looping an array
for i in array1:
    print(i)
[print(element) for element in array1]