def first_non_repeating(s):
    for i in range(len(s)):
        seen = True
        for j in range(len(s)):
            if i!=j and s[i]==s[j]:   
                seen= False
                break
        if seen:
            return i 
    return -1

print(first_non_repeating("KishantK"))


# i = 0 1 2 3 4 5 6 7 ..
# j =  0 1 2 3 4 5 6 7 ..


# k -2
# i - 1
# s - 1
# h - 1 


def first_non_repeating_opt(s):
    freq={}
    for char in s:
        freq[char] = freq.get(char,0)+1
    for i, char in enumerate(s):
        if freq[char]==1:
            return i
    return -1 

print(first_non_repeating_opt("KishantK"))
        
