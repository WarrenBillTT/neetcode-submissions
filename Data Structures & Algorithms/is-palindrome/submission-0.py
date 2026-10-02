class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for c in s:
            if c.isalnum():
                text += c.lower()
        return text == text[::-1]