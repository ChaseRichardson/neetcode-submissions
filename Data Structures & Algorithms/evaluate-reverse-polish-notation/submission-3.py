class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operands = {"+", "-", "*", "/"}
        

        for tok in tokens:

            if tok in operands:
                a = int(num_stack.pop())
                b = int(num_stack.pop())

                if tok == "+":
                    num_stack.append(a + b)
                
                elif tok == "-":
                    num_stack.append(b - a)
                
                elif tok == "*":
                    num_stack.append(a * b)

                else: num_stack.append(b / a)

            else: num_stack.append(tok)

        return int(num_stack[-1])


    

        
