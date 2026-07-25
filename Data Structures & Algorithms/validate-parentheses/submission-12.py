class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        maps={'(':')',  '{':'}',  '[':']'}
        
        for b in s:
            if b in maps:
                stack.append(maps[b])
            else:
                if stack :
                    if b == stack[-1]:
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
                
        
        if stack:
            return False
        else:
            return True