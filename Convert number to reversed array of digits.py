"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
"""

def digitize(n):
    l = [] # initialize an empty list
    for i in str(n): # convert the integer to a string and iterate through each character
        l.append(int(i)) # convert the character back to an integer and append it to the list
    return l[::-1] # return the reversed list
