'''
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

'''

def non_repeat_substring(str):

  start=0
  storage={} 
  Maxlength= -90
  for end in  range(len(str)):

    right_char = str[end]

    if right_char not in storage:
      storage[right_char]=end 
    else:

      start= storage[right_char]+1

    storage[right_char]=end  

    Maxlength= max(Maxlength, end-start+1)    


   
  return Maxlength

