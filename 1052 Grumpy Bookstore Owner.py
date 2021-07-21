class Solution:
    def maxSatisfied(self, customers, grumpy, X) :
        N = len(customers)
        res = sum([customers[i] * (1 - grumpy[i]) for i in range(N)])

        best_gain = sum([customers[i] * grumpy[i] for i in range(X)])

        gain = best_gain

        for i in range(X, N):
            gain += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            best_gain = max(gain, best_gain)

            i += 1

        return res + best_gain

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
a = Solution()
print(a.maxSatisfied(customers, grumpy, X))
