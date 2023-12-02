def decimalToBinary(n): 
    return bin(n).replace("0b", "")  #Normal: 0b101
print(decimalToBinary(5)) #after replace: 101


aile = ['yeman', 'aga']
aile[0] = aile[1]