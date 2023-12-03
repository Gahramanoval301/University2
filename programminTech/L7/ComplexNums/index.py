z1 = complex('7')
print(z1)
z2 = complex("7+17j")
# print('z2' + str(z2))
def DecimalToBinary(num):
        if num >= 1:
           print (num % 2, end="" )
           DecimalToBinary(num // 2)
DecimalToBinary(7)
print(sep='')
def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
print(decimalToBinary(7))

string = 'leman'
print(string[2:]) #slice method for python strings
print(type(oct(23)))
print(type(hex(12)))
print(float.hex(12.2))