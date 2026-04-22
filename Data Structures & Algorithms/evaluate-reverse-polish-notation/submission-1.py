class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","/","*","-"]
        stack = []

        for i in tokens :
            if i not in operators:
                stack.append(int(i))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if i == "+":
                    stack.append(num1+num2)
                elif i=="-":
                    stack.append(num2-num1)
                elif i=="*":
                    stack.append(num1*num2)
                elif i=="/":
                    stack.append(int(num2/num1))
        if len(stack)==1:
            return sum(stack)
        