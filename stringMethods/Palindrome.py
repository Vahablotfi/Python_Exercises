"""
Problem 2: Checking for a Palindrome
Explanation:
A palindrome is a word or phrase that reads the same forward and backward (e.g., "madam", "racecar"). We can check for palindromes using string slicing and conditionals.

Instructions:
1. Ask the user to enter a word.
2. Convert the word to lowercase to ensure case insensitivity.
3. Check if the word is the same when reversed.
4. Print "It's a palindrome!" if true, otherwise print "Not a palindrome."
"""

def isPalindrome(aString):
    '''
    aString: a string
    '''
    
    helper_var = ''
    for char in range(len(aString)-1, -1, -1):
        helper_var += aString[char]
        
    
    for char in range(len(aString)-1 ):
        if aString[char].lower() != helper_var[char].lower():
            return False
    return True

print (isPalindrome("raceCar"))
print (isPalindrome("madam"))
print(isPalindrome("dadash"))

        