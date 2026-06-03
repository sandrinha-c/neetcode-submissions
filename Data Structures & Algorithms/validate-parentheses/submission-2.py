class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left_bracket=["(","[","{"]
        for c in s:
            if c in left_bracket:
                if c == "(":
                    stack.append(')')
                elif c == "[":
                    stack.append(']')
                elif c == "{":
                    stack.append('}')
                print (stack)
            else:
                if not stack:
                    return False
                # elif c!= stack.pop():  can't pop first. 
                #     return False
                x=stack.pop()  
                print ('c=',c)
                print ('x=',x)  
                if c != x:
                    return False
        return not stack
      


        