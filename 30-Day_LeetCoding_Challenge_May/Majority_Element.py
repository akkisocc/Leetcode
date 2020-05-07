from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #m1 = Counter(nums)
        return Counter(nums).most_common(1)[0][0]
        
