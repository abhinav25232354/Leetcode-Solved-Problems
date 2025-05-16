class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                v = nums[i] + nums[j]
                if v == target:
                    return [i, j]

sol = Solution().twoSum([2, 7, 11, 15], 9)
print(sol)