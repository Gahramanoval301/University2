z1 = complex("7")
print(z1) #(7 + 0j)
# z2 = complex("2", "3")
# print(z2) #TypeError -> complex() can't take second arg if first is a string
z3 = complex("7+17j")
print(z3)
z4 = complex('7 + 17j') #ValueError
