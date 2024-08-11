# Q. Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

# Here are some examples to show how your function should work.

# >>> sumprimes([3,3,1,13])
# 19
# >>> sumprimes([2,4,6,9,11])
# 13
# >>> sumprimes([-3,1,6])
# 0


#------MY-SOLUTION------#
def factor(f):
    facList = []
    for i in range(1, f+1):
        if f%i == 0:
            facList = facList + [i]
    return facList

def isprime(p):
    if p <= 1:
        return 0
    elif factor(p) == [1, p]:
        return p
    else:
        return 0
    
def sumprimes(l):
    sum = 0
    for i in range(0, len(l)):
        sum = sum + isprime(l[i])
    return sum

print(sumprimes([2,4,6,9,11]))