class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        maps={}
        ans=[]
     
        
        for num in nums2:
            while stack and num>stack[-1]:
                key=stack.pop()
                maps[key]=num
            stack.append(num)
      

        for num1 in nums1:
            ans.append(maps.get(num1,-1))
        return ans