class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in a:
                if stack and stack[-1] == a[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 