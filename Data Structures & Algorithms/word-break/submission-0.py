class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        wordSet = set(wordDict)

        reachable = [False] * (n + 1)
        reachable[0] = True

        for i in range(1, n + 1):
            for word in wordSet:
                word_len = len(word)

                start = i - word_len

                if start < 0:
                    continue 
                
                if s[start:i] == word and reachable[start] == True:
                    reachable[i] = True
                    break

        return reachable[n]
        