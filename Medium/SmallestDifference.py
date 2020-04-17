***
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

Examples :

Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8} 
Output : 3  
That is, the pair (11, 8) 

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80} 
Output : 10
That is, the pair (40, 50)

Explaination: 
So bascially the naive approach here would be using two for lopps and scanning all the elements in both the Arrays.
However, the time complexity for that would be O(N^2). The more better approach would be to sort the arrays frist which take O(LogN) and then compare elements in both the arrya.

***


def findSmallestDifference(A,B,m,n):
    
    A.sort()
    B.sort()
    
    Diff=float('inf')
    i=m-1
    j=n-1
    
    while i>-1 and j>-1:
        
        if B[j]>=A[i]:
            Diff= min(abs(B[j]-A[i]), Diff)
            j-=1
        if B[j]<A[i]:
            Diff= min(abs(A[i]-B[j]), Diff)
            i-=1
            
    return Diff        
        
    
    
    
    
    
    
A = [1, 2, 11, 5] 
#After Sorting [1,2,5,11]
  
# Input given array B 
B = [4, 12, 19, 23, 127, 235]

  
# Calculate size of Both arrays 
m = len(A) 
n = len(B) 
  
# Call function to  
# print smallest result 
print(findSmallestDifference(A, B, m, n)) 
