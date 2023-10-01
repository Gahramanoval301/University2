yusif = 'yUsifA\t ü{isgood: 1}'
print(yusif.title())
print(yusif.capitalize())
print(yusif.casefold())  # make the lower case
print(yusif.center(20))  # make center within 20 space
print(yusif.count('y'))  # count occurence
print(yusif.encode())  # u is encoded
print(yusif.endswith('if'))
print(yusif.expandtabs(1))  # how much tabs put in \t
print(yusif.find('t'))  # if dont exists in string then return -1
print(yusif.index('y'))  # if dont exists in string then throw error
print(yusif.rindex('f'))  # finds the last occurrence of the specified value
# true if the string exists texts(chars)without e.c, format, or anything
print(yusif.isalnum())
print(yusif.isalpha())  # return true if only alhapet not any symbol and others
# empty string is ascii!! asci chraracters a-z(ascii table)
print(yusif.isascii())
# Check if all the characters in a string are decimals (0-9)
print(yusif.isdecimal())
print(yusif.isdigit())  # ², are also considered to be a digit.
# A valid identifier cannot start with a number, or contain any spaces.(a-z, 0-9, _)
print(yusif.isidentifier())
print(yusif.islower())
print(yusif.isnumeric())  # ² and ¾(true), -1 and 1.5(false)
print(yusif.isprintable())
print(yusif.isspace())  # true if all the characters in a string are whitespaces
print(yusif.isupper())
print(yusif.swapcase())  # lower case becomes upper and vice verca
balacaYusif = yusif.lower()
print(balacaYusif)
x = 'sayam'
print(yusif.join(x))  # it good for iterable elements
x = yusif.ljust(50)  # put the 50 space before 'salam' #rjust()
print(x, 'salam')
newyusif = '       bana naananana      '
# trim the spaces from left(l) #rstrip #strip
print('sayan', newyusif.lstrip(), 'i love uuuu')
print(yusif.maketrans('y', 'U', 'B'))  # return unicode codes
# we write in unicode and it translate them and replace
print(yusif.translate({65: 66}))
print(yusif.replace('y', 'Y'))
print(yusif.zfill(30))
# partitioned from left U and from the right U and U own
print(yusif.partition('U'))
# searches for the last occurrence of a specified string, and splits
print(yusif.rpartition('U'))
print(yusif.split())
print(yusif.rsplit())  # split from right(started from left)
print(yusif.splitlines())  # The splitting is done at line breaks.(\n)
# first character of words will upper case(if started num then the first char will be upper)
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

# {isgood:.2f} and isgood=2 then value will be change
print(yusif.format(isgood=2))
# print(yusif.format_map(''))  # ! aas follows
# input stored in variable a.
a = {'x': 'John', 'y': 'Wick'}

# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))
