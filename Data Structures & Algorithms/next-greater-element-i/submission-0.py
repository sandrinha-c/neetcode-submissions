class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        maps={}
        ans=[""]*len(nums1)
        
        for num in nums2:
            while stack and num>stack[-1]:
                key=stack.pop()
                maps[key]=maps.get(key,0)+num
            stack.append(num)
        while stack:
            remain_key=stack.pop()
            maps[remain_key]=maps.get(remain_key,-1)
    

          
        print (maps)
            
        #print (maps)
        for i, num1 in enumerate(nums1):
            if num1 in maps:
                ans[i]=maps[num1]
        return ans