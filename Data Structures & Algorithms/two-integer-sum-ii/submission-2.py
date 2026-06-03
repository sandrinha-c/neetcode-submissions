class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #naive
        for i in range (0,len(numbers)):
            num_1=numbers[i]
            for j in range (i+1,len(numbers)):
                num_2=numbers[j]
                result=num_1+num_2
                if result ==target:
                    return [i+1,j+1]



        