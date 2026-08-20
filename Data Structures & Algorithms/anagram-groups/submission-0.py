from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dicts = [dict(Counter(word)) for word in strs]
        word_pairs = list(zip(strs, word_dicts))
        print(word_pairs)
        sorted_list = sorted(word_pairs, key=lambda x: sorted(x[1].items()))
        result = []
        group = [sorted_list[0][0]]

        for i in range(1, len(sorted_list)) :
            if(sorted_list[i][1] == sorted_list[i-1][1]):
                group.append(sorted_list[i][0])
            else:
                result.append(group)
                group = [sorted_list[i][0]]
        
        result.append(group)
        return result