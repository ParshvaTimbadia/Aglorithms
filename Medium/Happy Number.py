'''
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3 ^22
​2
​​ +3
​2
​​  = 4 + 9 = 13
1^2 + 3^21
​2
​​ +3
​2
​​  = 1 + 9 = 10
1^2 + 0^21
​2
​​ +0
​2
​​  = 1 + 0 = 1
'''

def find_happy_number(n):
  # TODO: Write your code here


  result=0 
                
  while n > 0:
    rem = n % 10
    result = result + rem*rem
    n = n//10


    return result


  while sqrsum(n) not in list:
    num1= sqrsum(n)
    if num1==1:
      return True
    else:
      list.append(num1)
      n=num1
        
  return False
  


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()


