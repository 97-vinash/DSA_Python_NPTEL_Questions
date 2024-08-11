# Q. Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases.

# Here are some examples of how your function should work.

#   >>> contracting([9,2,7,3,1])
#   True

#   >>> contracting([-2,3,7,2,-1]) 
#   False

#   >>> contracting([10,7,4,1])
#   False


#------MY-SOLUTION------#
def contracting(l):
    myList = []
    for i in range(0, len(l)-1):
        diff = abs(l[i]-l[i+1])
        myList.append(diff)
  
    flag = True
    for i in range(0, len(myList)-1):
        if myList[i] <= myList[i+1]:
            flag = False
            break
  
    if flag == True:
        return(True)
    else:
        return(False)
    
print(contracting([9,2,7,3,1]))