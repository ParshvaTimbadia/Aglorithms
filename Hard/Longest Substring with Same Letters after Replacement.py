'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


'''
def length_of_longest_substring(str, k):
  # TODO: Write your code here

  window_start=0
  maxlength=0
  maxletter=0
  frequency_count={}

  for window_end in range(len(str)):
    right_char=str[window_end]
    if right_char not in frequency_count:
      frequency_count[right_char]=0
    frequency_count[right_char]+=1
    maxletter= max(maxletter, frequency_count[right_char])

    if (window_end - window_start +1 - maxletter) > k:
      left_char= str[window_start]
      frequency_count[left_char]-=1
      window_start+=1






    maxlength = max(maxlength, window_end - window_start+1) 




  return maxlength
