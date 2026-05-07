class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        for char in s:

            # keep appending to stack if (, [, {
            if char == '{' or char == '(' or char == '[':
                stack.append(char)

            elif char == '}' or char == ')' or char == ']':

                if stack and stack[-1] == '{' and char == '}':
                    stack.pop()

                elif stack and stack[-1] == '[' and char == ']':
                    stack.pop()

                elif stack and stack[-1] == '(' and char == ')':
                    stack.pop()

                else:         
                    return False

        if stack:
            return False

        return True

            