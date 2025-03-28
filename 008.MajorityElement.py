# Majority Element in an array

def majority_element(arr1):
    n = len(arr1)
    # print(n)
    # print(n//2)
    for num in arr1:
        if arr1.count(num)>n//2:
            return num
arr1=[1,1,2,24,24,24]
arr2 = [1,2,5,24,24,24,24]

def majority_optimal(arr1):
    candidate=arr1[0]
    count = 1
    for num in arr1[1:]:
        if count==0:
            candidate=num
        count+=1 if num ==candidate else -1
    return candidate
        
print(majority_optimal(arr1))   
    
    
print(majority_element(arr1))
