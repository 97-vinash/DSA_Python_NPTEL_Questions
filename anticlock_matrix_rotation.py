# Q. A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

#   1  2  3
#   4  5  6
#   7  8  9
# would be represented as [[1,2,3], [4,5,6], [7,8,9]].

# Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get

#   3  6  9
#   2  5  8    
#   1  4  7
# Your function should not modify the argument m provided to the function rotate().

# Here are some examples of how your function should work.

#   >>> leftrotate([[1,2],[3,4]])
#   [[2, 4], [1, 3]]

#   >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
#   [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

#   >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
#   [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


#------MY-SOLUTION------#
def leftrotate(m):
  size = len(m)
  transpose = [[0]*size for _ in range(size)]
    
  for i in range(0, size):
      for j in range(0, size):
          transpose[i][j] = m[j][i]
            
  rotated = [[0]*size for _ in range(size)]
  for i in range(0, size):
      size = size-1
      rotated[i] = transpose[size]
        
  return(rotated)

print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))