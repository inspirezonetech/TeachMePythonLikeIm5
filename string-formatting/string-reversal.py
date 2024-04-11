# ------------------------------------------------------------------------------------
# We're going to look at a few different ways that you can reverse the structure of a string .
# Let's begin.
# ------------------------------------------------------------------------------------

# Single Words , A string is an iterable and anything within these --> ""
# 1. The built-in reverse method
# This method is used on iterables , commonly on lists and strings
# Example of functions that reverse a string.
def reverseString(word):
    reversedWord = "".join(reversed(word))
    return reversedWord
'''
Let's break down what's above:
Remember that all strings are immutable but iterable. So if that's the case , we can't use the .reverse() function like we could on a list.
So we iterate through each letter and use the reversed() function . Now since the reversed() function return an iterable;a list .
We use the join() to concatenate the letters and then we return the reversed String.
'''
# 2.The reverse slice method
# This method also works on iterables too.
# Let's use the same example with this method too
def backString(word):
    reversedWord = word[::-1]
    return reversedWord
'''
Let's break this down as well:
The slicing technique is used to get a certain portion of string and using the starting and ending index values.
e.g [a:b], this slices from position to position before b ; so b-1 . What we don't commonly use is the third option of [a:b:c] <-- C.
What c does is specify the number of characters to jump or skip over . So if c == 2 , we're gonna skip over 2 characters .But if c == -1,this specifies that the string begins from the back.
We commonly use -1 when we want the last letter or character in a string e.g word = "pet",word[-1] == t.
Back to the function , if we don't specify the starting and end values , the computer just assumes it's the whole string .
So e.g [a:] this is from a to the last , [:b] from the first to b , [a::c] from a to the last every c characters , [:b:c] from the first to b every c characters .
So [::-1]  means from the first to last in reverse .
'''

# ------------------------------------------------------------------------------------
# The format is the same even for sentences : So write a function that reverses the sentence "I love ketchup".
