***
Problem Statement #
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]

A brute force solution could be to add all elements of the given ‘K’ lists to one list and sort it. If there are a total of ‘N’ elements in all the input lists, then the brute force solution will have a time complexity of O(N*logN)

Instead we can use MinHeap and the time complexity will get converted into O(N*Log K)
***


from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
    return self.value < other.value 


def merge_lists(lists):
  resultHead = None
  resultTail=None
  newnode=None
  minHeap =[]
  # TODO: Write your code here

  for root in lists:
    if root is not None:
      heappush(minHeap, root)

  while minHeap:
    newnode= heappop(minHeap)

    if resultHead is None:
      resultHead= resultTail = newnode
    else: 
      resultTail.next=newnode
      resultTail = resultTail.next

    if newnode.next is not None:
      heappush(minHeap, newnode.next)


    



  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

