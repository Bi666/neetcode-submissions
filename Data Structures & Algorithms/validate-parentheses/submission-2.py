class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()
        dic = {'(' : ')', '{' : '}', '[' : ']'}
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if stack and stack[-1] in dic and dic[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return False if stack else True