'''Converts the user input into scientific notation.'''
long = str(input("Enter a number to convert: "))
def convert(long):
    long = float(long)
    from decimal import Decimal
    return '%.4E' % Decimal(long)
print (convert(long))
