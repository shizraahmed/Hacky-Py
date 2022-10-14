import random


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))

password = uppercaseLetter1 + uppercaseLetter2
password = shuffle(password)

print(password)
