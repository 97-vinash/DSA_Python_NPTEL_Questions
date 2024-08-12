# Q. In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
# Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.

# Here are some examples to show how your function should work.

 
# >>> counthv([1,2,1,2,3,2,1])
# [2, 1]

# >>> counthv([1,2,3,1])
# [1, 0]

# >>> counthv([3,1,2,3])
# [0, 1]


#------MY-SOLUTION------#
def counthv(l):
  hill = 0
  vally = 0
  myList = []
  for i in range(1, len(l)-1):
      if l[i] > l[i+1] and l[i] > l[i-1]:
          hill = hill+1
      elif l[i] < l[i+1] and l[i] < l[i-1]:
          vally = vally+1
      else:
          continue
  myList.append(hill)
  myList.append(vally)

  return myList

print(counthv([1,2,1,2,3,2,1]))