class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps 

            for i in range(len(word)):
                for ch in alphabets:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, steps + 1))
                        visited.add(new_word)

        return 0
            
            
            
            







        