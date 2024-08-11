# Q. Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

#    Here are some examples of how your function should work.

#    >>> intreverse(783)
#    387
#    >>> intreverse(242789)
#    987242
#    >>> intreverse(3)
#    3


#------MY-SOLUTION------#
def intreverse (x):
    num_str1 = str(x)
    num_str2 = num_str1[::-1]
    reverseint = int(num_str2)
    return reverseint

print(intreverse(31511))