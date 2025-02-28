"""
Write a function called score that meets the specifications below.

def score(word, f):

   word, a string of length > 1 of alphabetical 
   characters (upper and lowercase)
   f, a function that takes in two int arguments and returns an int

   Returns the score of word as defined by the method:

   1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
   times its distance from start of word.  
   Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
   2) The score for a word is the result of applying f to the
   scores of the word's two highest scoring letters. 
   The first parameter to f is the highest letter score, 
   and the second parameter is the second highest letter score.
   Ex. If f returns the sum of its arguments, then the 
   score for 'adD' is 12 

"""

def score(word, f):
   """
   Computes the score of a word based on letter positions.

   The score of each letter is its position in the alphabet (a=1, b=2, ..., z=26)
   multiplied by its index in the word. The function `f` is applied to the two
   highest letter scores.

   Args:
      word (str): A string of length > 1 containing only alphabetical characters.
      f (function): A function that takes two integers and returns an integer.

   Returns:
      int: The final score of the word.

   Examples:
   >>> def add(a, b):
   ...     return a + b
   >>> score("adD", add)
   12

   >>> def multiply(a, b):
    ...     return a * b
   >>> score("adD", multiply)
   8

   >>> score("abc", add)  # (b=2*1, c=3*2) -> (2, 6), 2 + 6 = 8
   8

   >>> score("XYZ", add)  # (X=24*0, Y=25*1, Z=26*2) -> (26*2=52, 25*1=25), 52 + 25 = 77
   77

   >>> score("a", add)  # Only one letter -> 0
   0
   """




