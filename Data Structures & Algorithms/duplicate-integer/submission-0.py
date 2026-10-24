class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = {}
        for num in nums:
            if num in list:
                return True
            list[num] = list.get(num, 0) + 1
        return False