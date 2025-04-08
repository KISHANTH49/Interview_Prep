# apple -- a1e1l1p2

# aapppleee -- a2p3l1e3
def string_compress(s:str) ->str:
    if not s:
        return ""
    compressed =[]
    count = 1
    current = s[0]
    for i in range(1,len(s)):
        if s[i]== current:
            count+=1
        else:
            compressed.append(current+ str(count))
            current = s[i]
            count=1
    compressed.append(current+str(count))
    result= "".join(compressed)
    # return result 
    return result if len(result) < len(s) else s


print(string_compress("apple"))



def opt_string_compress(s:str) ->str:
    if not s:
        return ""
    result = ""
    count = 1
    current = s[0]
    for i in range(1,len(s)):
        if s[i]== current:
            count+=1
        else:
            result+= current+ str(count)
            current = s[i]
            count=1
    result+= current+ str(count)
    # return result 
    return result if len(result) < len(s) else s

print(opt_string_compress("apple"))
