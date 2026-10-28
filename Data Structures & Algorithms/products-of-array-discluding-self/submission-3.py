class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        result = []
        count = 0
        if 0 in nums:
            total = 0
            for num in nums:
                if num != 0:
                    if total == 0:
                        total += num
                        continue
                    total *= num
                else:
                    count += 1
            for j in range(len(nums)):
                if count > 1:
                    result.append(0)
                    continue
                if nums[j] != 0:
                    result.append(0)
                else:
                    result.append(int(total))
            return result
        for num in nums:
            total *= num
        for i in range(len(nums)):
            result.append(int(total/nums[i]))
        return result