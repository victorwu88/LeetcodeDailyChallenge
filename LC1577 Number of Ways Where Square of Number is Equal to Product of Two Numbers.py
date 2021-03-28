import collections
class Solution:
    def numTriplets(self, nums1, nums2) -> int:

        # brutal force won't work here
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)

        for i in nums1:
            d1[i * i] += 1

        for i in nums2:
            d2[i * i] += 1

        res = 0

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]

                res += d2[p]

        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                q = nums2[i] * nums2[j]

                res += d1[q]

        return res

nums1 = [7,4]
nums2 = [5,2,8,9]
a = Solution()
print(a.numTriplets(nums1, nums2))