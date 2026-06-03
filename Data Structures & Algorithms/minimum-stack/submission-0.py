class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            old_min= self.stack[-1][1]
            if val< old_min:
                new_min= val
            else:
                new_min=old_min
            self.stack.append((val, new_min))    
        

    def pop(self) -> None:
         self.stack.pop()
        

    def top(self) -> int:
         return (self.stack[-1][0])
        

    def getMin(self) -> int:
         return (self.stack[-1][1])
        
ms= MinStack()
ms.push(3)
print (ms.stack)
ms.push(5)
print(ms.stack)   # 期待 [(3, 3), (5, 3)]
ms.push(2)
print(ms.stack)   # 期待 [(3, 3), (5, 3), (2, 2)]
ms.pop()
print (ms.stack)
print (ms.stack[-1][0])
print (ms.top())
print (ms.getMin())