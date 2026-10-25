class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for p in s:
            if p ==  "]":
                if stack.pop() != "[":
                    return False
                else:
                    continue
            if p ==  "}":
                if stack.pop() != "{":
                    return False
                else:
                    continue
            if p ==  ")":
                if stack.pop() != "(":
                    return False
                else:
                    continue
            stack.append(p)
        return stack.pop() == 0
