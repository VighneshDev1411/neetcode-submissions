from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict1 = Counter(s)
        my_dict2 = Counter(t)

        lst1 = list(my_dict1.keys())
        lst2 = list(my_dict2.keys())
        lst3 = list(my_dict1.values())
        lst4 = list(my_dict2.values())
        
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst4.sort()

        print(lst1)
        print(lst2)
        print(lst3)
        print(lst4)

        

        if (lst1 == lst2 and lst3 == lst4):
            return True
        return False
