# Second Largest and largest

# 1,2,3,4,5,6

# Important Pointers : 
# 1. Are there any duplicates -- No duplicates -- Sort the array find n-1 and nth element
#  1,22,33,22,34,45,67,8  -- (1 ,22,33,34,45,67,8) -- array[1 ,22,33,34,45,67,8]-- sort() -- 1,8,22,34,45,67


# 2. We can convert this into a set - which will remove the duplicates -- again we will convert it into array/list and then print the elements + sorting

# largest , SecondLargest 

# l= -1 sl =-1   num = 40   l = 40 sl =-1

# l = 40 sl =-1   num =40   l = 80 sl = 40

# 40 40 40 40
# l = largest , sl = second_largest 
def largest_second_largest(arr):
    l = sl = float("-inf")

    for num in arr:
        if num >l :
            sl= l
            l = num
        elif num > sl and num !=l:
            sl = num
    return (l , sl if sl!=float("-inf") else -1)

    arr = [1 ,22,33,34,45,67,8]
    print(largest_second_largest(arr))

