'''Vowels

Five of the 26 English alphabet letters are vowels: A, E, I, O, and U. The string "SoloLearn" contains four vowels.

For example:
Input: "Welcome"
Output: 3 (e, o, and e are the vowels of the string "Welcome")

Input: "Hello, World!"
Output: 3 

Write a program that takes string input and outputs the count of the vowels in the string.
bonus: output number of digits in the string'''

text = str(input("Enter a word or phrase to be analyzed for vowel/digit content: \n"))
print ('Counting vowels and digits in ' + "'" + str(text) + "'")
def v_count(text):
    text= text.lower()
    vowels = ("a", "e", "i", "o", "u", "y")
    digits = ("0","1","2","3","4","5","6","7","8","9")
    v_count = 0
    d_count = 0
    for x in text:
        if x in vowels:
            v_count += 1
        if x in digits:
            d_count += 1
    #return v_count
    #return d_count
    print ("Vowel count:" + str(v_count))
    print ("Digit count:" + str(d_count))
(v_count(text))
