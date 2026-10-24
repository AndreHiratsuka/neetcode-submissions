class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer
                j += 1