'''
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false


'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  fast, slow= head, head
  while fast!=None and fast.next!= None:
    fast= fast.next.next
    slow= slow.next

  head_of_second_half= reverse(slow)
  copy_head_second_half = head_of_second_half

  while (head is not None and head_of_second_half is not None):
    if head.value != head_of_second_half.value:
      break  # not a palindrome

    head=head.next
    head_of_second_half= head_of_second_half.next  

  reverse(copy_head_second_half)
  
  if head is None or head_of_second_half is None:  # if both halves match
    return True

  return False

def reverse(head):

  prev= None
  while head is not None:
    later= head.next
    head.next= prev
    prev=head
    head = later

  return prev  


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()



