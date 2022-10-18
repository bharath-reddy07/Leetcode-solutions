import collections
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_value=0
        prev_max=0
        max_freq=0
        prev_max_freq=0
        while True:
            count=0
            prev_max_freq=max_freq
            prev_max=max_value
            max_value=max(nums)
            index_max=nums.index(max_value)
            length=len(nums)
            if length<=2:
                prev_max=max(nums)
                break
            frequency = collections.Counter(nums)
            
            max_freq=0
            for values in frequency.values():
                if values>max_freq:
                    max_freq=values
            print(max_freq,max_value)
            if prev_max_freq>max_freq :
                break
            nums[index_max]-=1
            nums[index_max-1]+=1
            
        return(prev_max)