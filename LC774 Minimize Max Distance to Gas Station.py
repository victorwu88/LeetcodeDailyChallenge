class Solution:
    def minmaxGasDist(self, stations, k: int) -> float:
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= k

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo
stations = [1,2,3,4,5,6,7,8,9,10]
k = 9
a = Solution()
print(a.minmaxGasDist(stations, k))