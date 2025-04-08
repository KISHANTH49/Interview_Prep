def reverse(s):
    result =""
    for i in range(len(s)-1,-1,-1):
        result+=s[i]
    return result

print(reverse("Kishanth"))

# K I S H A N T H 
# 0 1 2 3 4 5 6 7 
#           -2 -1

def reverse_opt(s):
    # return s[::-1]  # First Approach
    
    # Second Approach -- two Pointers
    s_list= list(s)
    left , right = 0 , len(s)-1
    while left < right:
        s_list[left],s_list[right]=s_list[right],s_list[left]
        left+=1
        right-=1
    return "".join(s_list)
print(reverse_opt("er"))

# Reverse the list by words 
# Hello World  -- World Hello 

# Split strings in words and then travrse using loops and reverse 
