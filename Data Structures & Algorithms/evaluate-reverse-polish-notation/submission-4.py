class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # List of valid operators in Reverse Polish Notation
        operators = ["+", "/", "*", "-"]
        
        # Stack to store numbers during evaluation
        stack = []

        # Traverse each token in the input list
        for i in tokens:
            # If the token is a number, convert to int and push onto stack
            if i not in operators:
                stack.append(int(i))
            else:
                # If the token is an operator, pop the top two elements
                # NOTE: Order matters for '-' and '/'
                num1 = stack.pop()  # top element (right operand)
                num2 = stack.pop()  # next element (left operand)

                # Perform operation based on the operator
                if i == "+":
                    stack.append(num2 + num1)
                elif i == "-":
                    stack.append(num2 - num1)  # subtraction: left - right
                elif i == "*":
                    stack.append(num2 * num1)
                elif i == "/":
                    # Division should truncate toward zero
                    stack.append(int(num2 / num1))

        # At the end, stack should contain exactly one result
        if len(stack) == 1:
            return stack[0]