class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Since the list is sorted, no three numbers can sum to zero
            # after the current number becomes positive.
            if nums[i] > 0:
                break

            # Avoid using the same value as the first number more than once.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Search only after i, guaranteeing three distinct indices.
            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # Move both pointers after finding a triplet.
                    j += 1
                    k -= 1

                    # Skip duplicate values on the left.
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values on the right.
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif current_sum < 0:
                    # We need a larger sum.
                    j += 1

                else:
                    # We need a smaller sum.
                    k -= 1

        return result