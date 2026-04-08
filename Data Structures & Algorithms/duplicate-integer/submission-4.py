class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = sorted(nums)
        for i in range(len(snums)-1):
            if snums[i] == snums[i+1]:
                return True
        return False