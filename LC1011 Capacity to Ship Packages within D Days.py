class Solution:
    def shipWithinDays(self, weights, D):

        left, right = max(weights), sum(weights)

        while left < right:
            mid, need, cur = (left + right) // 2, 1, 0

            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w

            if need > D:
                left = mid + 1
            else:
                right = mid

        return left
weights = [1,2,3,4,5,6,7,8,9,10]
D = 4
a = Solution()
print(a.shipWithinDays(weights, D))
