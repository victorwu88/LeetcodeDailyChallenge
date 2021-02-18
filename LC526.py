class Solution:
    count = 0

    def countArrangement(self, n: int) -> int:

        visited = [False] * (n + 1)
        self.calculate(n, 1, visited)
        return self.count

    def calculate(self, n, pos, visited):
        if pos > n:
            self.count += 1

        for i in range(1, n + 1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.calculate(n, pos + 1, visited)
                visited[i] = False

n = 5
a = Solution()
print(a.countArrangement(n))
