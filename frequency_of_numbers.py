# Q. Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

# minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
# Here are some examples of how your function should work.

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12])
# ([7], [13])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
# ([7], [13, 14])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
# ([7, 11, 12], [13, 14])


# I COULDN'T SOLVE IT, BECAUSE I WAS NOT VERY FAMILIER WITH DICTIONARIES

#------GIVEN-SOLUTION------#
def frequency(l):
    count = {}
    for n in l:
        if n in count.keys():
            count[n] = count[n]+1
        else:
            count[n] = 1
    minlist = findmin(count)
    maxlist = findmax(count)
    return((minlist,maxlist))

def findmin(d):
    upperbound = 0
    for n in d.keys():
        if d[n] > upperbound:
            upperbound = d[n]

    minlist = []
    mincount = upperbound

    for n in d.keys():
        if d[n] < mincount:
            minlist = [n]
            mincount = d[n]
        elif d[n] == mincount:
            minlist.append(n)
    return(sorted(minlist))

            
def findmax(d):
    maxlist = []
    maxcount = 0

    for n in d.keys():
        if d[n] > maxcount:
            maxlist = [n]
            maxcount = d[n]
        elif d[n] == maxcount:
            maxlist.append(n)
    return(sorted(maxlist))

print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]))