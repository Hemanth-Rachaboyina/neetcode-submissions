from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Left and right pointers for the sliding window
        l = 0
        r = 0

        # Frequency map of characters in t (what we need to match)
        d = Counter(t)

        # Length of the smallest valid window found
        answer_length = float("inf")

        # 'formed' = how many unique characters currently satisfy required frequency
        # 'total' = total unique characters we need to satisfy
        formed, total = 0, len(d)

        # Store the best window boundaries
        subl, subr = 0, 0

        # Expand the window using right pointer
        while r < len(s):
            char = s[r]

            # If current character is needed
            if char in d:
                d[char] -= 1

                # If frequency becomes exactly zero, requirement for this char is met
                if d[char] == 0:
                    formed += 1

            # Try to shrink the window from the left if all requirements are met
            while l <= r and formed == total:
                curr_len = r - l + 1

                # Update the smallest window if current is smaller
                if curr_len < answer_length:
                    answer_length = curr_len
                    subl, subr = l, r + 1  # store window boundaries

                # Remove the leftmost character from the window
                char = s[l]
                if char in d:
                    # If removing breaks a valid requirement, reduce formed count
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1

                # Move left pointer forward
                l += 1

            # Expand window by moving right pointer
            r += 1

        # If no valid window found, return empty string
        return "" if answer_length == float("inf") else s[subl:subr]