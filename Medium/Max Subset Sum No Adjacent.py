'''
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.

Examples :

Input : arr[] = {5, 5, 10, 100, 10, 5}
Output : 110

Input : arr[] = {1, 2, 3}
Output : 4

Input : arr[] = {1, 20, 3}
Output : 20Max 
'''

def find_max_sum(arr): 
    
    if not len(arr):
        return
    elif len(arr)==1:
        return arr[0]
    
    MaxSum = arr[:]
    MaxSum[1]= max(MaxSum[0], MaxSum[1])
    
    for i in range(2,len(arr)):
        MaxSum[i]= max(MaxSum[i-1], MaxSum[i-2]+ arr[i])
    
    return MaxSum[-1]
        
  

arr = [5, 5, 10, 100, 10, 5] 
print (find_max_sum(arr)) 
