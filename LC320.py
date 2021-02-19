class Solution:
    def generateAbbreviations(self, word):
        res = []
        self.backtrack(word, [], 0, 0, res)

        return res

    def backtrack(self, word, cur, pos, cnt, res):
        if pos == len(word):
            if cnt:
                cur.append(str(cnt))

            res.append("".join(cur))

            return

        self.backtrack(word, cur, pos + 1, cnt + 1, res)

        cur.pop()

        if cnt:
            cur.append(str(cnt))

        self.backtrack(word, cur + [word[pos]], pos + 1, 0, res)

if __name__ == '__main__':
    word = 'Ma'
    a = Solution()
    print(a.generateAbbreviations(word))