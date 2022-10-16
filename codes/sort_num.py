#Program to sort list of numbers entered by user (least to greatest)
#would appreciate any input on using sys.argv to get the program to pull input off the command line

x = input('Enter a list of numbers separated by a comma\n')
x = x.split(',')
def sort(x):
    y  = []
    for i in x:
        y.append(int(i))
    y.sort()
    print (y)
sort(x)
