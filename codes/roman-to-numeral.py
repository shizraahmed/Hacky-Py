str = input("Enter Roman Numberal ")
str = str.upper()
num = 0
index = 0
while index != (len(str)):
    if str[index] == "I":
        if index < (len(str) - 1):
            if str[index + 1] == "V":
                num = num + 4
                index = index + 2
            elif str[index + 1] == "X":
                num = num + 9
                index = index + 2
            else:
                num = num + 1
                index = index + 1
        else:
            num = num + 1
            index = index + 1
    elif str[index] == "V":
        num = num + 5
        index = index + 1
    elif str[index] == "X":
        if index < (len(str) - 1):
            if str[index + 1] == "L":
                num = num + 40
                index = index + 2
            elif str[index + 1] == "C":
                num = num + 90
                index = index + 2
            else:
                num = num + 10
                index = index + 1
        else:
            num = num + 10
            index = index + 1
    elif str[index] == "L":
        num = num + 50
        index = index + 1
    elif str[index] == "C":
        if index < (len(str) - 1):
            if str[index + 1] == "D":
                num = num + 400
                index = index + 2
            elif str[index + 1] == "M":
                num = num + 900
                index = index + 2
            else:
                num = num + 100
                index = index + 1
        else:
            num = num + 100
            index = index + 1
    elif str[index] == "D":
        num = num + 500
        index = index + 1
    elif str[index] == "M":
        num = num + 1000
        index = index + 1
print(num)
