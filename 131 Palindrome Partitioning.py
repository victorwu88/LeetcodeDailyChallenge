class Solution:
    def partition(self, s: str):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    s = 'aab'
    a = Solution()
    print(a.partition(s))
