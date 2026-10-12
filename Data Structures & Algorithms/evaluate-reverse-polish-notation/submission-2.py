class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        opps = ['+', '-', '*', '/']
        for x in tokens:
            if x not in opps:
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == opps[0]:
                    stack.append(a+b)
                elif x == opps[1]:
                    stack.append(b-a)
                elif x == opps[2]:
                    stack.append(a * b)
                else:
                    stack.append(int(b/a))
        return stack[-1]



            


        