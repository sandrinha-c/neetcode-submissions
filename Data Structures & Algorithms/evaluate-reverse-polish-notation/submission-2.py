class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if len(tokens)==1:
                return int(token)
            if stack and token in ("+","-","*","/"):
                a=int(stack.pop())
                b=int(stack.pop())
                if token=="+":
                    result=b+a
                elif token=="-":
                    result=b-a
                elif token=="*":
                    result=b*a
                elif token=="/":
                    result=int(b/a)
                stack.append(result)
            else:
                stack.append(token)
        return result