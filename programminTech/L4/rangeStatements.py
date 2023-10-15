
#? -------Python Membership Operators--------------------------------
#! in and not in
animals = ('aga', 'leman', 'cat', 'dog')
if 'aga' in animals:
    print('aga is in the animals list')
if 'kitty' not in animals:
    print('kitty is not in the animals list')    
#?--------------------------------Range Statement----------------------
#* from 0 to 5
for i in range(6):
    print(i)
print('--------------------------------')
# range(start, stop, step)
# Parameter	Description
# start	Optional. . Default is 0
# stop	Required. (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1
#* from 1 to 5
for i in range(1, 5):
    if(i== 3):
        continue
    print(i)

