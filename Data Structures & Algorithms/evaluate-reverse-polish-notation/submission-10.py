class Solution:
    # idea is to add to stack, and once we reach 2 numbers, just folow the operation
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            # addition
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            # subtraction, note we must reverse, not assosciative in a sense
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            # multiply
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            # division
            elif i == "/":
                c, d = stack.pop(), stack.pop()
                stack.append(int(d/c))
            else:
                stack.append(int(i))
            
        return stack[0]

