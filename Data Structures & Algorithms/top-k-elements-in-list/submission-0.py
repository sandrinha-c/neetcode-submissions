class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        for num in nums:
            nums_dict[num]=nums_dict.get(num,0)+1
        result=sorted(nums_dict.items(), key=lambda x:x[1], reverse=True) # need .items()! and key!
        #print([result[0][0],result[1][0]])
        result_list=[]
        for i in range(k):
            result_list.append(result[i][0])
        return result_list
