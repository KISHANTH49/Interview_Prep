def prod(arr):
    product =1 
    for num in arr:
        product*=num
       
    for i in range(len(arr)):
        arr[i]=int(product/arr[i])
    print(arr)
    
arr = [2,3,4,5,7]

prod(arr)

#  The Approach assumes there are only number >0
