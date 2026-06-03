class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min=1
        k_max=max(piles)
   
        while (k_min <= k_max): #k max跟min之前還有東西嗎
            k= (k_min+k_max)//2
            hr_acc=0
            for p in piles:
                if p%k==0:
                    hr_p= p//k
                else:
                    hr_p=(p//k)+1
                hr_acc+=hr_p
            if hr_acc> h:  #t 太大 所以要 increase k 所以k min=k
                k_min= k+1  
            elif hr_acc <=h: #t 小於h, 看看t可不可以在更小 (k可不可以更大) kmax=k mid
                ans=k
                k_max=k-1
        return ans
    
                
        