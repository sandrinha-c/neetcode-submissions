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
                        print('here1')
                        return False 
                else:
                    print('here2')
                    return False
                
        
        if stack:
            print('here3')
            return False
        else:
            return True