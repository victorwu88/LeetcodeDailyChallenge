class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1

            else:
                hi = mi

        return lo
piles = [3,6,7,11]
h = 8
a = Solution()
print(a.minEatingSpeed(piles,h))
