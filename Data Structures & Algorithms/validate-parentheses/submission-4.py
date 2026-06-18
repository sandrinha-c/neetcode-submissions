class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opens=['(',  '{',  '[' ]
        maps={
            ')':'(', 
            '}': '{', 
            ']' :'['
            }
        for item in s:
            if item in opens:
                stack.append(item)
            else:
                if stack:
                    if maps[item]==stack[-1]:
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
        if not stack:
            return True
        else:
            return False
                