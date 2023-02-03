"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""


def get_middle(s):
    l=len(s)
    if l==1 or l==2:
        return s
    elif l%2==0:
        m=l//2
        print(m)
        return s[m-1:m+1]
    else:
        m=l//2
        return s[m]
