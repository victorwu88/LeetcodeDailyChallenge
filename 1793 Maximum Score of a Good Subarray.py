class Solution:
    def maximumScore(self, nums, k) -> int:

        left, right = [], []
        minn = nums[k]
        for i in range(k, -1, -1):
            minn = min(minn, nums[i])
            left.append(minn)

        minn = nums[k]
        for i in range(k, len(nums)):
            minn = min(minn, nums[i])
            right.append(minn)

        res = 0
        i, j = 0, len(nums) - 1

        while left and right:
            res = max(res, (j - i + 1) * min(left[-1], right[-1]))

            if left[-1] < right[-1]:
                left.pop()
                i += 1

            else:
                right.pop()
                j -= 1

        return res
nums = [1,4,3,7,4,5]
k = 3
a = Solution()
print(a.maximumScore(nums, k))
