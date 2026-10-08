class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        
        i = 0
        while i+1 < len(nums):
            if nums_sorted[i] == nums_sorted[i++1]:
                return True
            i+=1
        return False