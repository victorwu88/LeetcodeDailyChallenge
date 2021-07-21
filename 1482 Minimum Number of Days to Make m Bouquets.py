class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:

        if m * k > len(bloomDay): return -1
        left, right = 1, max(bloomDay)
        while left < right:

            mid = (left + right) // 2
            flower = bouq = 0

            for day in bloomDay:
                flower = 0 if day > mid else flower + 1
                if flower >= k:
                    flower = 0
                    bouq += 1

                    if bouq == m: break

            if bouq == m:
                right = mid

            else:
                left = mid + 1

        return left
bloomDay = [1,10,3,10,2]
m = 3
k = 1
a = Solution()
print(a.minDays(bloomDay, m, k))
