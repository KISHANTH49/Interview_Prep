# [tea , ate ,eat] -- e a t
# a e t --  a  e t - a e t 
# kin , ink , nik -- i n k 


# ["eat"-["tea","ate","eat"]]
def group_anagrams(strs:list[str])->list[list[str]]:
    anagram_map={}
    for s in strs:
        # s.lowercase()
        # sorted_string = "".join(sorted(s.lowercase()))
        sorted_string = "".join(sorted(s))
        if sorted_string in anagram_map:
            anagram_map[sorted_string].append(s)
        else:
            anagram_map[sorted_string]=[s]
        return list(anagram_map.values())

strs = ["eat","ant","tea","ate","tan","pea","ape","tin"]
# print(group_anagrams(strs))   


# anagram_map={}
#  eat -- sorted -- a e t 
'''
anagram_map{
    "aet":["eat","tea","ate"],
    "ant":["ant","tan"],
    "aep":["pea","ape"],
    "int:["tin"]
}
'''

'''
anagram_map{ 
     a       e                t
    "1 0 0 0 1 0 0 0 0 0 0 ..  1 0 0 0 0 0 ":["eat","tea","ate"],
    "1 0 0 0  0 0 0 0 0 0 1..  1 0 0 0 0 0":["ant","tan","nat"],
    "aep":["pea","ape"],
    "int:["tin"]
}
'''
from collections import defaultdict
def opt_anagrams_group(strs:list[str])->list[list[str]]:
    # 97 101
    # 101 - 97 =5
    # 97 -97 
    anagram_map=defaultdict(list)
    for s in strs:
        char_count =[0]*26
        #  1 0 0 0 0 0 0 0 0 0 0     1--26
        #  a b c d e f g h i j k l m n
        for char in s:
            char_count[ord(char)-ord('a')]+=1
        
        key = tuple(char_count)
        anagram_map[key].append(s)
    return list(anagram_map.values())

strs = ["eat","ant","tea","ate","tan","pea","ape","tin"]
print(opt_anagrams_group(strs)) 


