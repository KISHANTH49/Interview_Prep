# Intersection of arrays
def intersection(arr1, arr2):
    result = []
    for num in arr1:
        if num in arr2 and num not in result:
            result.append(num)
    
    return result 

def intersection_2(arr1,arr2):
    set1 = set(arr1)
    result = set()
    for num in arr2:
        if num in set1:
            result.add(num)
    return list(result)
arr1=[1,1,2,10]
arr2 = [1,2,5,9.10,24]
print(intersection_2(arr1,arr2))            
print(intersection(arr1,arr2))
          
