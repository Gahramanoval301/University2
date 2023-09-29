number1 = float(input('Enter the first num:'))
number2 = float(input('Enter the second num:'))
sum = number1 + number2
print("Sum is " + str(sum))
# Python can't concenate the string and float(int)
# Python can't conversion from int to float!
weight = float(input('Enter weight: '))
LorK = input('(K)g or (L)bs')
if LorK == 'K':
    print(weight*100)
elif LorK == 'L':
    print(weight/10)
    print('Done')
