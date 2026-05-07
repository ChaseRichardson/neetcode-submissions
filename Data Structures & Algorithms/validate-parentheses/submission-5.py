class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        it = 0

        while it < len(s):

            # keep appending to stack if (, [, {
            if s[it] == '{' or s[it] == '(' or s[it] == '[':
                stack.append(s[it])

            elif s[it] == '}' or s[it] == ')' or s[it] == ']':

                if stack and stack[-1] == '{' and s[it] == '}':
                    stack.pop()

                elif stack and stack[-1] == '[' and s[it] == ']':
                    stack.pop()

                elif stack and stack[-1] == '(' and s[it] == ')':
                    stack.pop()

                else:
                    
                    return False

            it += 1

        if len(stack) > 0:
            print(stack)
            return False

        return True

            