'''
Smallest Window containing Substring (hard) #
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.



,

'''


def find_substring(str, pattern):
  window_start=0
  match=0
  minimum_length=len(str)+1
  frequency_count={}
  startpointer=0

  for i in range(len(pattern)):
    chr= pattern[i]
    if chr not in frequency_count:
      frequency_count[chr]=0
    frequency_count[chr]+=1
 

  #Trying to extend the range 
  for window_end in range(len(str)):
    right_char= str[window_end]
    if right_char in frequency_count:
      frequency_count[right_char]-=1

      if frequency_count[right_char]>=0:
        match+=1
        


    while match == len(pattern):
  # Save the current window and store it:
      if minimum_length > window_end -window_start +1:
        minimum_length = window_end - window_start +1
        startpointer= window_start
    
    #Shrink the window     

      left_char=str[window_start]

      window_start+=1

      if left_char in frequency_count:
        
        if frequency_count[left_char]==0:
          match-=1
        frequency_count[left_char]+=1

        

  if minimum_length > len(str):
    return ""
  return str[startpointer:startpointer + minimum_length]
  







