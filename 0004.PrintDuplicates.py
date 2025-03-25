# find duplicates and print them 


# [2,3,4,5,3,5,7]

# [3,5]

def find_duplicates(arr2):
    duplicates=[3,5]
    for i in range(len(arr2)):
        for j in range(i+1,len(arr2)):
            if arr2[i]==arr2[j] and arr2[i] not in duplicates:
                duplicates.append(arr2[i])
    return duplicates
arr2= [2,3,4,5,3,5,7]               
print(find_duplicates(arr2))







 
 
