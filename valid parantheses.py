class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        map={')': '(',']':'[','}':'{'}
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map:
                if not stack or stack[-1] !=map[char]:
                    return False
                stack.pop()
            else:
                continue
        return len(stack) == 0