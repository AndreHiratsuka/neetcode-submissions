class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            print(f"low = {low}, mid = {mid}, high = {high}, number = {nums[mid]}")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1