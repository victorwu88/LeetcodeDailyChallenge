class Solution:
    def maxSum(self, nums1, nums2) -> int:

        mod = 10 ** 9 + 7
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        sa = sb = ans = 0

        while i < n and j < m:

            if nums1[i] < nums2[j]:
                # move forward in nums1, and add this value to sum
                sa = sa + nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                # move forward in nums2, and add this value to sum
                sb = sb + nums2[j]
                j += 1

            else:
                # nums1[i] == nums2[j]
                # we take the larger of the two sa, sb
                ans = ans + max(sa, sb) + nums1[i]
                # sa, sb = 0 since a new segment starts after this;
                sa = sb = 0
                i += 1
                j += 1

        while i < n:
            # just in case the array is not completed
            sa = sa + nums1[i]
            i += 1

        while j < m:
            sb = sb + nums2[j]
            j += 1

        # bigger of the two
        ans = (ans + max(sa, sb)) % mod
        return ans
nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]
a = Solution()
print(a.maxSum(nums1, nums2))