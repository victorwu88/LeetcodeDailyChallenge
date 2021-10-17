class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            print(L)
            if index == 0:
                step = 1

            elif index == numRows - 1:
                step -= 1

            index += step

        return "".join(L)


a = Solution()
s = 'PAYPALISHIRING'
numRows = 3
print(a.convert(s, numRows))

