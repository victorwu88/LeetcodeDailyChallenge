class Solution:
    def maximizeSweetness(self, sweetness, K) -> int:

        left, right = 1, sum(sweetness) // (K + 1)
        while left < right:
            mid = (left + right) // 2

            cur = cuts = 0

            for sweet in sweetness:
                cur += sweet
                if cur > mid:
                    cuts += 1
                    cur = 0

            if cuts > K:
                left = mid + 1

            else:
                right = mid

        return right

sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
a = Solution()
print(a.maximizeSweetness(sweetness, K))
