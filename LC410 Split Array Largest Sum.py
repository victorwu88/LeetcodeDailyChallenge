class Solution:
    def splitArray(self, nums, m: int) -> int:

        l, r = 0, 0
        n = len(nums)
        for i in range(n):
            r += nums[i]
            if l < nums[i]:
                l = nums[i]

        ans = r
        while l <= r:
            mid = (l + r) // 2
            sum = 0
            cnt = 1
            for i in range(n):
                if sum + nums[i] > mid:
                    cnt += 1
                    sum = nums[i]

                else:
                    sum += nums[i]

            if cnt <= m:
                ans = min(ans, mid)
                r = mid - 1

            else:
                l = mid + 1

        return ans
nums = [7,2,5,10,8]
m = 2
a = Solution()
print(a.splitArray(nums, m))