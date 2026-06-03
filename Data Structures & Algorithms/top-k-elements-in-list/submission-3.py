class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        #build dict {num: freq}
        for num in nums:
            nums_dict[num]=nums_dict.get(num,0)+1
        print ("nums_dict:",nums_dict)

        #build buckets [[],[]------] number is postion, inside [] is freq
        buckets= [[]for _ in range(len (nums)+1)] # concept of buckets!!!
        for num, freq in nums_dict.items():
            buckets[freq].append(num)
        print ("buckets:",buckets)

        #back traverse/extract number from buckets:
        freq_list=[]
        for freqs in reversed (buckets):
            if freqs: #true if bucket [freq] is NOT empty
                for freq in freqs:
                    freq_list.append(freq)
                    if len(freq_list)==k:
                        return freq_list
    