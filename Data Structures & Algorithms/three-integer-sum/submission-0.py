class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force 
        memory= set()# tuple set to avoid duplicate
        
        for i in range (len (nums)):
            for j in range (i+1, len(nums)):
                for k in range (j+1, len (nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp_memo=[nums[i],nums[j],nums[k]]
                        memory.add(tuple(sorted(temp_memo)))
                        print (memory)
        return list(memory)

                

            
            

        