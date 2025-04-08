def Palindrome(s):
    newString = [c.lower() for c in s if c.isalnum()]
    left , right = 0 , len(newString)-1
    while left < right:
        if newString[left]!= newString[right]:
            return False
        left+=1
        right-=1
    return True

print(Palindrome("Kishanth"))
