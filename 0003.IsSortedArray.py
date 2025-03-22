def Is_sorted_array(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:   # 2>3
                return False
        return True

arr = [2,3,6,7,8]
print(Is_sorted_array(arr))

# Dry Run -- 
def Is_sorted_array_op(arr):
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            return False
        return True


# Find the sum of all the numbers of an array 
# Average of all the elements of the array
# Product of the elements 

# Prodcut of every element except the element itself
# arr = [2,3,4]   
# arr = [12,8,6]

# Replace every element with its square


        

