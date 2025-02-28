"""
Replacing Vowels in a String
Explanation:
We can replace characters in a string using loops and conditional statements. 
This example replaces all vowels in a string with *.

Instructions:
1. Ask the user to enter a sentence.
2. Replace all vowels (a, e, i, o, u) with *.
3. Print the modified sentence.

Example Usage:
    Input:  "Hello World"
    Output: "H*ll* W*rld"

    Input:  "AEIOU aeio u"
    Output: "***** *****"

"""


vowels = "auioeAUIOE"

sentence = input("Please type a sentence : ")

new_sentence = ''

for char in sentence:
    if char in vowels:
        new_sentence += '*'
    else:
        new_sentence += char
        
print("modified sentence: ", new_sentence)