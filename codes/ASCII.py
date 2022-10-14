# Print the ASCII value 
from distutils.log import error

while True:
    print("Enter a Key: ")
    try:
        val = input()

        print("Your Input: %s"%val)
        
        # print  ASCII value  
        print("The ASCII value of '"+val+"'is", ord(val))
    except :
    
        print("A error occurred,try again.")
