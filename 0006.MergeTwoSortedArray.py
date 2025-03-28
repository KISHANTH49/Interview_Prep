# Merge two Sorted arrays

# arr= [1,2,5,6,7,9,10,24]

# sorted()

# print(sorted(arr1+ arr2))

def merge_optimal(arr1, arr2):
    result =[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
arr1 = [1,2,5,8,24,24,24,24,24]
arr2= [6,9,10,24,24,45,90]
# print(merge_optimal(arr1, arr2))

