class Solution:
    def numSubseq(self, nums, target) -> int:

        nums.sort()
        N = len(nums)
        res = 0
        l, r = 0, N - 1
        mod = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1

            else:
                res += pow(2, r - l, mod)

                l += 1

        return res % mod

nums = [3,5,6,7]
target = 9
a = Solution()
print(a.numSubseq(nums, target))