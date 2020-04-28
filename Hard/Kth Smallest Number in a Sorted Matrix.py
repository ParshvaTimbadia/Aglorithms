***

Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
***


from heapq import *

def find_Kth_smallest(matrix, k):
  number = -1
  minHeap = []
  counter=0
  
  for i in range(len(matrix)):
    heappush(minHeap, (matrix[i][0], 0, matrix[i]))

  print (minHeap)  

  while minHeap:
    number, i , row = heappop(minHeap)

    counter+=1

    if i+1 < len(row):
      i+=1
      heappush(minHeap, (row[i] , i, row))

    if counter==k:
      return number  



  


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
