class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:

        def condition(divisor) -> bool:
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

nums = [1,2,5,9]
threshold = 6
a = Solution()
print(a.smallestDivisor(nums, threshold))
