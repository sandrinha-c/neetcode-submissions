class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pos_tme=[]
        for pos, spd in zip(position, speed):
            pos_tme.append((pos, ((target-pos)/spd)))
        pos_tme.sort(reverse=True)
        print (pos_tme)
        for car in pos_tme:
            car_arrive_tme=car[1]
            if not stack:
                stack.append(car)
            elif car_arrive_tme > stack[-1][1]: #>prev car arrive time
                stack.append (car)
                print (stack)
            
        return (len(stack))
                
                
