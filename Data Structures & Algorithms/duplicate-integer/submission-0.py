class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store=[]
        for num in nums:
            if num not in store: 
                store.append(num)
            else:
                return True 
        return False
               
            

