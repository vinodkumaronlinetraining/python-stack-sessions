# arr=[7, 5, 4, 8, 2, 1]
# n= len(arr) = 6
# i = 0 (range(n-1)), j= 0 (range(n-1-i))

# step1: arr[j] > arr[j+1], 7>5, [5, 7, 4, 8, 2, 1]
# j = 1, arr[1]>arr[2], 7>4, [5, 4, 7, 8, 2, 1]
# j=2, arr[2]>arr[3], 7>8, no, [5, 4, 7, 8, 2, 1]
# j=3, arr[3] > arr[4], 8>2, [5,4,7,2,8,1]
# j=4, arr[4]>arr[5], 8>1, [5,4,7,2,1,8]


# step2: i=1, j=0, [ 5,4,7,2,1,8], j (range(n-1-i)) 
# j=0, arr[0]>arr[1], 5>4, [4,5,7,2,1,8]
# j= 1, arr[1]> arr[2], 5>7, no, [4, 5, 7, 2, 1, 8]
# j=2, arr[2]>arr[3], 7>2, [ 4,5,2,7,1,8]
# j=3, arr[3]>arr[4], 7>1, [4,5,2,1,7,8]



# step3, i= 2, j=0, [4,5,2,1,7,8] j(range(6-1-2))
# j= 0, arr[0]>arr[1], 4>5, [4,5,2,1,7,8]
# j= 1, arr[1]>arr[2], 5>2, [4,2,5,1,7,8]
# j=2, arr[2]>arr[3], 5>1, [4,2,1,5,7,8]

# step4: 1= 3, j= 0, [ 4,2,1,5,7,8] range(6-1-3=2)
# j=0, arr[0]>arr[1], 4>2, [2,4,1,5,7,8]
# j=1, arr[1]>arr[2], 4>1, [2,1,4,5,7,8]

# step5: i=4, j= 0, [2,1,4,5,7,8] range(6-1-4)
# j=0, arr[0]>arr[1], 2>1, [1,2,4,5,7,8]

# step6: i=5, j=0(range(6-1-5))
# [1,2,4,5,7,8]

# def bubble_sort(arr):
#     n =len(arr)
#     for i in range(n-1):
#         for j in range(0,n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# arr = [7,3,5,1,9,0,3,5]
# print(bubble_sort(arr))


#  passes n (n)=  n *n = time complexity O(n^2)
# O(n) 

# space complexity= O(1)


# def sort_numbers(nums):
#     n= len(nums)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if nums[j]>nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

# print(sort_numbers([5,2,3,1]))


# [12, 11,13,5,6]
# i = 1, key[i] = 11, j= i-1=0
# j >=0, arr[j] > key, [12, 12, 13, 5, 6], arr[j+1] = arr[j], j = j-1
# j = -1, arr[j+1] = key, [11, 12, 13, 5, 6]

# step2: i=2, key[i] = 13, j=i-1=1
# j >=0, arr[j] > key, 12 >13, [11, 12, 13, 5, 6]

# step3: i=3, key[3]=5, j=3-1=2
# j >=0, arr[j]>key, 13>5, arr[j+1] = arr[j], [11,12,13,13,6], j=j-1=1
# j>=0, arr[j]>key, 12>5, arr[j+1] = arr[j], [11, 12, 12, 13, 6] j=0
# j>=0, arr[j]>key, 11>5, arr[j+1] = arr[j], [11, 11, 12, 13, 6] j=-1
# j =-1, arr[j+1] = key, [ 5, 11, 12, 13, 6]

# step4: i=4, key[4]=6, j=i-1=3
# j>=0, arr[j] >key, 13>6, arr[j+1] = arr[j], [5,11,12,13,13] j=2
# j >=0, arr[j]>key, 12>6, arr[j+1] = arr[j], [5,11,12,12, 13] j=1
# j >=0, arr[j]>key, 11>6, arr[j+1] = arr[j], [5,11,11,12,13] j =0
# j>=0, arr[j]>key, 5>6, false, [5, 11,11,12,13]  
# j = 0, arr[j+1] = key, arr[1] = 6, [5,6,11,12,13]

# final output: [ 5,6,11,12,13]

# time complexity : n * n = O(n^2)
# space complexity: O(1)

# def insertion_sort(arr):
#     n =len(arr)
#     for i in range(1,n):
#         key = arr[i]
#         j = i-1
#         while j>=0 and arr[j]> key:
#             arr[j+1] = arr [j]
#             j = j -1
#         arr[j+1] = key
#     return arr

# print(insertion_sort([3,7,1,8,0,3]))
        
# selection sort

# [64, 25, 12, 22, 11]
# i = 0, min_idx = i =0, j=i+1=1  , min_idx[0]=64, 25, 12, 11
# arr[i], arr[min_idx]= arr[min_idx], arr[i], [11, 25, 12, 22, 64]

# step2: i =1, j= i+1= 2, min_idx[i]=25, 12,
# swap min_idx=12, i=25  , [11, 12, 25, 22, 64]

# step3: i=2, j= 3, min_idx[i]= 25, 22
# swap min_idx=22, i=25,   [11, 12, 22, 25, 64]

# step4 i=3, j=4, min_idx[i]=25, 
# [11, 12, 22, 25, 64]

# def selection_sort(input_nums):
#     n = len(input_nums)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if input_nums[j]< input_nums[min_idx]:
#                 min_idx = j
#         input_nums[i], input_nums[min_idx] = input_nums[min_idx], input_nums[i]
#     return input_nums

# # arr = [64, 25, 12, 22, 11]
# # print(selection_sort(arr))

# # step1: n step2: n  n*n o(n^2)
# # space : O(1)

# def max_difference(input_nums):
#     sorted_array = selection_sort(input_nums)

#     # [2,3,4,5,6,7]
#     # (arr[-1]*arr[-2])-(arr[0]*arr[1])

#     return (sorted_array[-1]*sorted_array[-2])-(sorted_array[0]*sorted_array[1])

# print("initial array [5,6,2,7,4]")
# print("max_difference:",max_difference([5,6,2,7,4]))

# print("initial array:[4,2,5,9,7,4,8]")
# print("max_difference:",max_difference([4,2,5,9,7,4,8]))

# Merge sort:

# [ 38, 27, 48, 3, 9, 82, 10] 7//2=3.5=3
# L[38, 27, 48]      R[3, 9, 82, 10]
# L[38]  R[27, 48]
# L[38]  L[27]  R [48]
#          R[27,48]
# L[27, 38, 48]

#R[3, 9, 82, 10]
# L[3,9] R[82, 10]
# L[3] R[9]
# L[3, 9]  L[82] R[10]
# L[3,9]   R[10, 82]
# R[3, 9, 10, 82]

# L[27, 38, 48]   R[3, 9, 10, 82]
# [3, 9, 10, 27, 38, 48, 82 ]

# [ 38, 27, 48, 3, 9, 82, 10] n = len(arr)
# mid = 7//2,= 3, L=[38, 27, 48] R= [3,9,82,10]


# L[38]  L[27]  R [48]
# i=j=k=0, arr[k],
# i< len(L), j<len(R) , l[0] <r[0] , arr[0]= l[0], i=1, k=1
#   arr[k] = R[j] [27, 48]

# def merge_sort(arr):
#     if len(arr)>1:
#         mid = len(arr)//2
#         L= arr[:mid]
#         R = arr[mid:]

#         merge_sort(L)
#         merge_sort(R)

#         i = j = k =0

#         while i <len(L) and j <len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i] # [1,2,3]
#                 i +=1
#             else: 
#                 arr[k] = R[j]
#                 j +=1
#             k +=1

#         while i <len(L):
#             arr[k] = L[i]
#             i +=1
#             k+=1

#         while j <len(R):
#             arr[k] = R[j]
#             j +=1
#             k +=1

#     return arr

# arr= [ 38, 27, 48, 3, 9, 82, 10]
# print(merge_sort(arr))


# time: log n * n= O(n log n)
# space: n = O(n)


# num1 = [1,2,3] m= 3 num2 = [2,5,6] n=3
# num1 = [_,_,_,_,_,_]
# def merge(num1, m, num2, n):
    
#     p1 = m-1  # considers the last value of first list
#     p2 = n-1 # considers the last value of second list
#     p = m+n -1 # considers the last position in the sorted array

#     while p1 >= 0 and p2 >=0:
#         if num1[p1]> num2[p2]:
#             num1[p] = num1[p1]
#             p1 -=1
#         else:
#             num1[p] = num2[p2]
#             p2 -=1
#         p -=1

#     while p2 >=0:
#         num1[p] = num2[p2]
#         p2 -=1
#         p -=1
#     return num1

# print(merge([ 1,2,3,0,0,0], 3,[2,5,6] , 3))

# arr = [2,2,3,3,4,4,5,5,7,8,9]

# num = list(set(arr))

# print(num)

# quick sort:

# arr = [3, 6, 8, 10, 1, 2, 1] n
# step 1:
# 7//2= 3.5= 3 index= 10
# left = [3, 6, 8, 1, 2, 1]
# right = []
# mid = [10]
# left[3,6,8,1,2,1] mid = [10] right = []

# step2: [3,6,8,1,2,1]
# 6//2= 3, pivot = 1
# left = []
# mid = [1,1]
# right = [3, 6, 8, 2]
# left = [] mid = [1,1] right = [3,6,8,2]

# step3: [3,6,8,2]
# 4//2 = 2, pivot = 8
# left = [3,6,2]
# mid = [8]
# right = []
# left = [3,6,2] mid = [8] right = []

# step4:[3,6,2]
# 3//2 = 1, pivot = 6
# left = [3,2]
# mid = [6]
# right = []
# [3,2] [6] []

#step5: [3,2]
# 2//2 = 1, pivot = 2
# left = []
# mid =[2]
# right = [3]
# [] [2] [3]

# [2,3]
# [ 2,3,6]
# [ 2,3,6,8]
# [1,1,2,3,6,8]
#[1,1,2,3,6,8, 10]


def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[len(arr)//2] # arr[7//2]= arr[3] = 3
        left = [x for x in arr if x <pivot]
        right = [x for x in arr if x> pivot]
        mid = [ x for x in arr if x == pivot]
        return quick_sort(left)+ mid + quick_sort(right)
    
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))

# [3,10,2,1]
# pivot = 3
# left = [2,1]
# mid = [3]
# right = [10]
# [2,1] [ 3] [10]

#[2,1]
# pivot = 1
# left = []
# mid = [1]
# right = [2]
# [ ] [1] [2]

# [1,2, 3, 10]

# log n * n = O(nlogn)

# log n = 0(logn)

# tim sort: merge sort and insertion sort

# arr = [5, 21, 3, 8,12,1,9,14,7,16] or [2,21,3]
# min_run = 4, n = len(arr) = 10
# 
# for loop: i= range( 0,n,min_run )= (0,10,4)=  [5,21,3,8] [12,1,9,14] [7, 16]
# start = 0, end = min(3,  10-1)= 3, insertion_sort(arr, 0,3)
# start = 4, end = min(start +mid-1, n-1)=(4+ 4-1, 9)= 7 insertion_sort(arr, 4, 7)
# Start = 8, end min(start+mid-1, n-1) = (8+4-1, 9)=(11,9)= 9 [7,16] insertion_sort(arr, 8, 9)
#  [3,5,8,21]  [1,9,12,14] [7,16]

def insertion_sort(arr, start, end):
    for i in range(start+1, end+1):
        key = arr[i]
        j = i-1
        while j >= start and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def merge_sort(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1: right]

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i+1
        else:
            arr[k] = right_arr[j]
            j = j+1

        k +=1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i +=1
        k +=1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
    
    return arr

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run-1, n-1)

        insertion_sort(arr, start, end)

    size = min_run

    while size < n: # 4<3
        for left in range(0,n,2 * size ):
            mid = min(left +size-1, n-1)
            right = min(left +2*size-1, n-1)

            if mid < right:
                merge_sort(arr, left, mid, right)

        size *=2
    return arr

arr = [5, 21, 3,5,2,7,9,1,5,7,9,12,76,12]
print(tim_sort(arr))