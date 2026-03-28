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


# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     else:
#         pivot = arr[len(arr)//2] # arr[7//2]= arr[3] = 3
#         left = [x for x in arr if x <pivot]
#         right = [x for x in arr if x> pivot]
#         mid = [ x for x in arr if x == pivot]
#         return quick_sort(left)+ mid + quick_sort(right)
    
# arr = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(arr))

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
#---------------------------------------------------------
# tim sort: merge sort and insertion sort

# arr = [5, 21, 3, 8,12,1,9,14,7,16]  or [4,3,9]
# 5,21,3,8   12,1,9,14    7,16
# [3,5,8,21,   1,9,12,14 ,   7,16]  Insertion sort output
# [1,3,5,8,9,12,14,21]    7,16
# 1,3,5,7,8,9,12,14,16,21

# min_run = 4
# for start in range(0,n,min_run): # 4 # 8
#       end = (start + min_run-1) # (0+ 4-1)=3 # (4 + 4 -1)=7 # (8+4-1)=11 , n-1 =9
#       end = min(start+min_run-1, n-1)

#       insertion_sort(arr, start, end)
#
# for left in range(0, n,2* min_run ) # 0,8
#       right = (left + 2*size-1) = (0+7)=7, (8+7)=15 = min(left+ 2*size-1, n-1)
#       mid = (left + size-1,n-1)
#       merge_sort(arr, left, mid, right)
#

def insertion_sort(arr, start, end):
    for i in range(start+1, end+1):
        key = arr[i]
        j = i-1
        while j>= start and arr[j]> key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def merge_sort(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i=j=0
    k= left
    while i <len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i+1
        else:
            arr[k] = right_arr[j]
            j = j+1
        k +=1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
    return arr

def tim_sort(arr):
    min_run = 4
    n = len(arr)

    for start in range(0,n,min_run):
        end = min(start+min_run-1, n-1)
        insertion_sort(arr, start, end)

    size = min_run

    while size < n:
        for left in range(0, n, 2*size):
            mid = min(left + size-1, n-1)
            right = min(left+ 2*size -1, n-1)

            if mid < right:
                merge_sort(arr, left, mid, right)
        size *=2 
    return arr

# arr = [5, 21, 3, 10,32,65,2,5,8,9,1,6,8]
# print(tim_sort(arr))

# sorted_list1 = sorted(arr) # create a new array and store result
# sortted_list2 = arr.sort() # sort the elements in the the existing array

# print(sorted_list1)
# print(sortted_list2)
# print(arr)

# time: logn * n =O(nlogn)
# space: O(n) O(1)

#----------------------------------------------------------------
# searching algorithms : 

# [5,3,2,8,1]
# target 10

# # Linear search:
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [5,3,2,8,1]
# print(linear_search(arr,10))

#time: best case-O(1), worst=O(n)
# space: O(1)


# #[1,1,2,3,3,4,4,6,6,7,7] or [1]
# def duplicates(nums):
#     n = len(nums)
#     for i in range(0,n,2 ):
#         if i+1 >=n or nums[i] != nums[i+1]:
#             return f"index:{i}, value:{nums[i]}"
#     return -1

# arr = [1,1,3,4,4,7,7]
# print(duplicates(arr))

#-----------------------
# Binary search:

# [1,2,3,4,5,6,7,8,9] target=7
# left = 0, right = 8
# mid = left + (right - left) //2 = 0+8//2= 4 arr[mid] == target , 5 == 7
# arr[mid] < target: 5 < 7, left  = mid +1, 5
# mid = left+ (right-left)//2, 5+(8-5)/
# 

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = left + (right -left) //2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else: 
#             right = mid-1
#     return -1

# arr = [-1,0,3,5,9,12]
# print(binary_search(arr, 9))

# # logn
# # best case: O(1), logn


# Tree:
#---------------------------------------------
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# root  = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(20)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(1)

# def print_tree(root):
#     if not root:
#         return
#     queue = [root]
#     while queue:
#         current = queue.pop(0)
#         print(current.value)
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)

# print_tree(root)

         
# Binary search tree:
#--------------------------------

# class TreeNode:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     # inserting values to the tree:
#     def insert(self, value):
#         if not self.root:
#             self.root = TreeNode(value)
#         else:
#             self._insert(self.root, value)

#     def _insert(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self._insert(node.right, value)

#     def search(self, target):
#         return self._search(self.root, target, steps=1)
    
#     def _search(self, node, target, steps):
#         if node is None:
#             print(f"Not found after {steps -1} comparisons")
#             return False
#         print(f" Step {steps}: visiting {node.value}: ")

#         if target == node.value:
#             print(f"Found Target {target}")
#             return True
#         elif target < node.value:
#             print(f"{target} < {node.value}, go to Left")
#             return self._search(node.left, target, steps +1)
#         else: 
#             print(f"{target}> {node.value}, Go to Right")
#             return self._search(node.right, target, steps +1)
        
# bst = BinarySearchTree()
# for val in [10,5,15,3,7,12,20]:
#     bst.insert(val)

# print("\nSearching for target 7\n")
# bst.search(7)

# print("\n searching for 2\n" )
# bst.search(2)

# Checking if an input array is a valid binary tree:
#--------------------------------------
# [10,5,15,3,7,12,20]
#[5,4, 1, none] 

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Build the tree:
# class BuildTree:
#     def build_tree(self, arr):
#         if not arr:
#             return None
#         root = TreeNode(arr[0])
#         queue = [root]
#         i = 1
#         while queue and i < len(arr):
#             current = queue.pop(0)
#             if i < len(arr) and arr[i] is not None:
#                 current.left = TreeNode(arr[i])
#                 queue.append(current.left)
#             i +=1
#             if i< len(arr) and arr[i] is not None:
#                 current.right = TreeNode(arr[i])
#                 queue.append(current.right)
#             i +=1
#         return root
    
# class Solution:
#     def is_valid_bst(self, root:TreeNode) -> bool:
#         def validation(node, min_val, max_val):
#             if node is None:
#                 return True
#             if node.value <= min_val or node.value >= max_val:
#                 return False
#             return validation(node.left, min_val, node.value) and validation(node.right, node.value, max_val)
#         return validation(root, float('-inf'), float('inf'))

# input1 = [10,5,15,3,7,12,20]
# input2 = [8,3,12,None,None]
# build = BuildTree()
# tree1 = build.build_tree(input1)
# tree2 = build.build_tree(input2)         

# solution = Solution()
# print(solution.is_valid_bst(tree1))
# print(solution.is_valid_bst(tree2))

#-----------------------
# stack and queue:

# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D", "E"],
#     "C": ["A","F"],
#     "D": ["B"],
#     "E": ["B"],
#     "F": ["C"]

# }

# # Breadth first search:
# from collections import deque

# def bfs(graph, start, target):
#     queue = deque([start])
#     visited = set(start)

#     while queue:
#         node = queue.popleft()
#         print(f"Visiting the node: {node}")

#         if node == target:
#             print(f"Found target: {target}")
#             return True
#         for neighbours in graph[node]:
#             if neighbours not in visited:
#                 visited.add(neighbours)
#                 queue.append(neighbours)

#         print(f"Queue: {list(queue)}")
#     print(f"Target {target} is not found")
#     return False

# graph = {
    # "A": ["B", "C"],
    # "B": ["A", "D", "E"],
    # "C": ["A","F"],
    # "D": ["B"],
    # "E": ["B"],
    # "F": ["C"]

# }
# bfs(graph, "A", "G")


# from collections import deque
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def build_tree(arr): # [3,5,7,3,8]
#     if not arr:
#         return None
#     root = TreeNode(arr[0])
#     queue = [root]
#     i =1
#     while queue and i<len(arr):
#         current = queue.pop(0)
#         if i < len(arr) and arr[i] is not None:
#             current.left = TreeNode(arr[i])
#             queue.append(current.left)
#         i +=1
#         if i < len(arr) and arr[i] is not None:
#             current.right = TreeNode(arr[i])
#             queue.append(current.right)
#         i +=1
#     return root

# def bfs_tree(root, target):
#     if not root:
#         return False
    
#     queue = deque([root])

#     while queue:
#         node  = queue.popleft()
#         print(f" Visiting : {node.value}")

#         if node.value == target:
#             print(f"Found target: {target}")
#             return True
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#         print(f"Queue: {[n.value for n in queue]}")

#     print(f"Target {target} not found")
#     return False

# input = [1,2,3,4,5]
# root = build_tree(input)
# bfs_tree(root,5)

#             # 1
#         # 2       3
#     # 4     5

# Depth first search:
#---------------------------------------

# def dfs(graph, start, target, visited=None):
#     if visited is None:
#         visited = set()

#     print(f"Visiting: {start}")

#     if start == target:
#         print(f"Found Target: {target}")
#         return True
#     visited.add(start)

#     for neighbour in graph[start]:
#         if neighbour not in visited:
#             if dfs(graph,neighbour,target, visited):
#                 return True
        
#         print(f"Backpropagating from: {neighbour} to {start}")
#     print(f"Backpropagating to {start}")
#     return False

# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D", "E"],
#     "C": ["A","F"],
#     "D": ["B"],
#     "E": ["B"],
#     "F": ["C"]
# }

# dfs(graph, "A", "F")

#                     # A
#                 #B        C
#         #   D      E          F



# # DFS with trees:
# from collections import deque
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def build_tree(arr): # [3,5,7,3,8]
#     if not arr:
#         return None
#     root = TreeNode(arr[0])
#     queue = [root]
#     i =1
#     while queue and i<len(arr):
#         current = queue.pop(0)
#         if i < len(arr) and arr[i] is not None:
#             current.left = TreeNode(arr[i])
#             queue.append(current.left)
#         i +=1
#         if i < len(arr) and arr[i] is not None:
#             current.right = TreeNode(arr[i])
#             queue.append(current.right)
#         i +=1
#     return root

# def dfs_tree(node, target, visited=None):
#     if node is None:
#         return False
    
#     if visited is None:
#         visited = set()
#     print(f"Visiting: {node.value}")
#     if node.value == target:
#         print(f"Found Target:{target}")
#         return True
#     visited.add(node)

#     if node.left and node.left not in visited:
#         if dfs_tree(node.left,target, visited):
#             return True
    
#     if node.right and node.right not in visited:
#         if dfs_tree(node.right, target, visited):
#             return True
        
#     print(f"Backpropagating from the node: {node.value}")
#     return False

# input = [1,2,3,4,5]
# tree = build_tree(input)
# dfs_tree(tree, 5)
# #             # 1
# #         # 2       3
# #     # 4     5

# Hash map:
#-------------------------------------------
# person = {

# }
# person["name"] = "Vinod"   hash["name"]   0 : Vinod
# person["city"] = "Hyd"     hash["city"]   2: hyd

# print(person)

# class HashMap:
#     def __init__(self):
#         self.map = {}

#     def put(self, key, value):
#         self.map[key] = value

#     def get(self,key):
#         return self.map.get(key, None)
    
#     def remove(self, key):
#         if key in self.map:
#             del self.map[key]

#     def contains_key(self,key):
#         return key in self.map
    
#     def size(self):
#         return len(self.map)

# hash_map = HashMap()
# hash_map.put("name", "Vinod")
# hash_map.put("city", "hyd")
# print(hash_map.get("name"))
# print(hash_map.get("city"))
# hash_map.remove("city")
# print(hash_map.contains_key("name"))
# print(hash_map.contains_key("city"))
# print(hash_map.size())

#---------------------------------------
# count the no of occurances of each word in a sentence:
# This is python stack session and this is batch one
# word: 1

# def word_frequency(input):
#     frequency = {}

#     for word in input.lower().split():
#         if word in frequency:
#             frequency[word] +=1
#         else:
#             frequency[word] = 1  

#     return frequency

# text = "This is python stack session and this is batch one"
# print(word_frequency(text))

#-----------------------------------------

# input array,[1,2,3,4,7] contains numbers, target = 10, 
# 10-1 = 9 
# 10-2 = 8
# 10-3 = 7+3

# def target_sum(input, target):
#     seen = {}

#     for i, num in enumerate(input):
#         temp_value = target - num

#         if temp_value in seen:
#             return [seen[temp_value], i]
        
#         seen[num] = i

#     return []

# print(target_sum([1,2,3,4,7], 0))


#time and space complexity:

# Binary search:
# in each step the no of searches is reduciong, complexity reducing: O(logn)
# space O(1) O(logn)

# bfs:
# bfs in trees
# time: O(nodes)
# space O(nodes)

# graph:
# time: O(node+connections)
# space: O(levels or no of connections)


# dfs:

#trees- time: O(node )   space:O(nodes)

# graph: time:O(node+connections)
# space: O(levels or no of connections)


# Hash:
# time: O(1), worst case: O(n)

# name: vinod, 

# space: O(n)


# [1,2,3,4,5,6,7,8,9]  = [1] -> [2] ->  [3] -> [4]-> [5]

# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def append(self,value):
#         new_node = ListNode(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def prepend(self,value):
#         new_node = ListNode(value)
#         if not self.head: # if the list is empty
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#     def find(self, value):
#         current = self.head
#         previous = None
#         while current:
#             if current.value == value:
#                 return current
#             current = current.next
#         return None
#     def delete(self, value):
#         current = self.head
#         previous = None
#         while current:
#             if current.value == value:
#                 if previous:
#                     previous.next = current.next
#                 else:
#                     self.head = current.next
#                 if current == self.tail:
#                     self.tail = previous
#                 return True
#             previous = current
#             current = current.next
#         return False
    
# sample_list = SinglyLinkedList()
# sample_list.append(1)
# sample_list.append(2)
# sample_list.append(3)
# print(sample_list.find(1).value)
# sample_list.prepend(0)
# print(sample_list.find(0).value)
# sample_list.delete(2)
# print(sample_list.find(2))

# class DoubleLinkListNode:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None

# class DoubleLinkList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = DoubleLinkListNode(value)
#         if not self.head:
#             self.head = new_node
#             self.tail =new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node

#     def prepend(self, value):
#         new_node = DoubleLinkListNode(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def find(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 return current
#             current = current.next
#         return None
    
#     def delete(self, value):
#         current = self.head
#         while current:
#             if current.value ==  value:
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.head = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 else:
#                     self.tail = current.prev
#                 return True
#             current = current.next
#         return False

# double_list = DoubleLinkList()
# double_list.append(1)
# double_list.append(2)
# double_list.append(3)
# print(double_list.find(2).value)
# double_list.prepend(0)
# print(double_list.find(0).value)
# # double_list.delete(3)
# print(double_list.find(3).value)

# time: append-O(1), delete-O(n) , find-O(n)
# space: append(O(n)), O(1)


# # Dynamic programming:
# #---------------------------
# # number 1:  result = 5      1+1+1+1+1 = 5
# # number 1: result = 7       1+1+1+1+1+1+1 =7, 5+1+1= 7

# # fib 0 = 0
# # fib 1 = 1
# # fib 2 = fib(2-1) + fib(2-2) = 1+0 = 1
# # fib 3 = fib(3-1) + fib(3-2) + fib(3-3) = 1+1+0=2
# # fib n = fib(n-1) + fib(n-2)

# # top down approach:
# def fibonacci_series(n, data={}):
#     if n in data:
#         return data[n]
#     if n <=1:
#         return n
#     data[n] = fibonacci_series(n-1, data) + fibonacci_series(n-2,data)
#     return data[n]

# print(fibonacci_series(10))

# # - data[4] = fibonacci_series(3, data) + fib_ser(2,data)
# #- fib_ser(3) = fib_ser(2)+fib_ser(1)= fib_ser(2)+ 1 = 1+1= 2
# #- fib_(2) = fib_ser(1)+ fib_ser(0)= 1+0 = 1
# # step1: data[4] = fib_3 +fib_2 = 2 + 1 = 3


# def fib_ser(n): #fib_ser(10)
#     if n <=1:
#         return n
#     fib_table = [0]*(n+1) # [0,0,0,0,0,0,0,0,0,0,0]
#     fib_table[1] = 1  # [0,1,0,0,0,0,0,0,0...]
#     for i in range(2, n+1):
#         fib_table[i] = fib_table[i-1] + fib_table[i-2] #
#     return fib_table[n], fib_table

# # while i = 2, fib_table[2] = fib_table[1] + fib_table[0] = 1+0 = 1   [0,1,1,0,0,0...]
# # i= 3, fib_tabe[3] = fib_table[2] + fib_table[1] = 1+1=2     [0,1,1,2,3,5,8,13,21,34]
# # i = 10 fib_table[10] = fib_table[9] + fib_table[8] = 34 + 21 = 55   [0,1,1,2,3,5,8,13,21,34,55]
# print(fib_ser(10))


# stairs n: ways to climb steps are 1, 2.   

# 5
# 1. 1+1+1+1+1 = 5
# 2. 1+1+1+2  = 5
# 3. 1+1+2+1
# 4. 1+2+1+1
# 5. 2+1+1+1
# 6. 2+2+1
# 7. 2+1+2
# 8. 1+2+2

def climb(n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2 # 1. 1+1, 2. 2
    dp = [0]* (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(climb(8))

# time: O(n)
# space: O(n)