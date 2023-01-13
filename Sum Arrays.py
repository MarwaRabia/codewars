"""
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

"""

from functools import reduce

def sum_array(x):
    # Check if the input list is empty
    if len(x)==0:
        return 0
    # Use the reduce function to sum up all elements in the list
    x=reduce(lambda a,b:a+b,x)
    # Return the sum
    return x
