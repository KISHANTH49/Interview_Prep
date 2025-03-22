# 1,2,3,4,6,7,8

# 0 1 2 3 4 5 6 7 8

# Sort the array
# take the difference between value and  index 

# for any point of time , the diff goes > 1 
# Then we have got the element - arr[index]-1 = 5

# def find_missing_number(arr,n):
#     num_set = set(arr)
#     for i in range(1,n+1):    #
#         if i not in num_set:
#             return i 
#     return -1
# arr = [1,2,3,4,6,7,8]  
# print(find_missing_number(arr,8)) 


# set -- 1,2,6,4,3,7,8 

# sum of natuarl numbers = n * (n+1)//2

# 1 3 4 -- 4   4*(5)//2 = 10 - 8 =2 
# def find_missing_number(arr,n):
#     total = (n*(n+1))//2
#     return total - sum(arr)
# arr = [1 ,3, 4]
# print(find_missing_number(arr,4))

def sum_array(arr):
    sum =0                             #  sum = 4 
    for i in range(len(arr)):            # i =0
        sum+=arr[i]      # sum = sum + arr[i] = 4 +4=  8
    return sum

arr = [1 ,3, 4]
print(sum_array(arr))

def product_array(arr):
    sum =1                             #  sum = 1 
    for i in range(len(arr)):            # i =0
        sum*=arr[i]      # sum = sum* arr[i] = 1
    return sum

arr = [1 ,3, 4]
print(product_array(arr))