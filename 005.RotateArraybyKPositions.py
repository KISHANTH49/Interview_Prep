# Rotate an Array by K rotations / Positions
#  arr = [2,3,4,5,7]
#  [5,7,2,3,4]

# Reverse complete array - Split the arrays into two parts -- reverse both arrays seperatly -- combine them
# [2,3,4,5,7].  --- 21st 
# 7,5     4,3,2
# 5,7,2,3,4 
# 

# first time -- 7 2 3 4 5
# second -      5 7 2 3 4 
#    3          4 5 7 2 3
#   4           3 4 5 7 2 
# 5             2 3 4 5 7

def rotate_array(arr,k):
    def reverse(arr, start,end):
        while start <end:
            arr[start] , arr[end]= arr[end] , arr[start]
            start+=1
            end-=1
    k = k% len(arr)
    n = len(arr)
    reverse(arr, 0 , n-1) # COmplete array reverasal - 0 - 5 == 2, 3,4,5,7
    reverse(arr, 0, k-1)  # 7,5 -- 5,7
    reverse(arr, k, n-1)    # 4,3,2. -- 2,3,4
    return arr            # 5 7 2 3 4 

arr = [2,3,4,5,7]  
print(rotate_array(arr,2))



# [2,3,4,5,7] --  = k= 2
# 2 , 7= 7,2
# 7 ,3,4 ,5 2

#  7,5         4,3 ,2
