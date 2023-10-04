name = 'Leman'
# first_name = name[1] // L
first_name = name[1:4]
# first_name = name[1:] 1 den axira qeder
# first_name = name[1:4:2] 2deneden bir slice ele
# reversed_name = name[::-1]; /tersine duzur
# slice = slice(2, 6)  # !
# slice = slice(2, -1) #!
print(name[slice(1, 2)])  # !
# print(name[slice])  # !
print(first_name)
