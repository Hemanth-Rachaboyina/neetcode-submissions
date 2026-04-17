class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():   # keeps only letters and digits
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]