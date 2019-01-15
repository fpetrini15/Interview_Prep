'''
3. Longest Substring Without Repeating Characters
Medium

4560

227

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        count = 0
        maximum = 0
        Q = deque()
        if s == " ":
            return 1
        for elt in s:
            if elt not in Q:
                Q.append(elt)
                maximum = max(maximum, len(Q))
            else:
                maximum = max(maximum, len(Q))
                while Q.popleft() != elt:
                    continue
                Q.append(elt)
        return maximum
            
                