class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dih = {}

        for i in nums:
            if dih.get(i) == 1:
                return True
            dih[i] = 1
        return False