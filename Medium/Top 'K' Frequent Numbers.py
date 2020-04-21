***
Problem Statement #
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.


***



from heapq import *
def find_k_frequent_numbers(nums, k):
  topNumbers = []
  dict={}

  for i in nums:
    if i not in dict:
      dict[i]=0
    dict[i]+=1

  min_heap=[]
  for key, value in dict.items():
    print(min_heap)
    heappush(min_heap, [value, key])
    if len(min_heap)>k:
      heappop(min_heap)


  while min_heap:
    topNumbers.append(heappop(min_heap)[1])

    




  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
