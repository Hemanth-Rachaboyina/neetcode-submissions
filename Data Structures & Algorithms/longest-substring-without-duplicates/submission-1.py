class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Left pointer of the sliding window
        l = 0
        
        # Set to store unique characters in the current window
        sett = set()
        
        # Variable to store the maximum length found
        res = 0
        
        # Right pointer moves through the string
        for r in range(len(s)):
            
            # If current character is already in the set,
            # shrink the window from the left until it's removed
            while s[r] in sett:
                sett.remove(s[l])  # remove leftmost character
                l += 1             # move left pointer forward
            
            # Add current character to the set
            sett.add(s[r])
            
            # Update the result with the current window size
            # (r - l + 1) is the length of the current substring
            res = max(res, r - l + 1)
        
        # Return the maximum length of substring without repeating characters
        return res