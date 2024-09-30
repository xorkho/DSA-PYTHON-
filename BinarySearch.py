# #LAB 1
# #QUES:1
# # from timeit import default_timer as timer
# # def BinarySearch(arr,query):
# #     low=0
# #     high=len(arr)-1
# #     while low<=high:
# #         mid=(low+high)//2
# #         if arr[mid]==query:
# #             return mid
# #         elif arr[mid]<query:
# #             low=mid+1
# #         else:
# #             high=mid-1
# #     return "not found"

# # def builtin_search(arr,query):
# #     return arr.index(query)

# # start=timer()
# # print(BinarySearch([3,4,5,6,7,8,9],8))
# # end=timer()
# # print(f"total time of my binary search is {round((end-start),6)} sec")

# # start=timer()
# # print(builtin_search([3,4,5,6,7,8,9],8))
# # end=timer()
# # print(f"total time of binary search is {round((end-start),6)} sec")

# #QUES:2
# def check_sort(l):
#     min=l[0]
#     for i in range(1,len(l)):
#         if min<=l[i]:
#             min=l[i]
#         else:
#             return False
#     return True

# def insert_item(l,low,query):
#     new_list=l[0:low]
#     new_list+=[query]
#     new_list2=l[low:len(l)]
#     inserted=new_list+new_list2
#     return inserted

# def BinarySearch(arr,query):
#     sorted_array=check_sort(arr)
#     if sorted_array==True:
#         low=0
#         high=len(arr)-1
#         while low<=high:
#             mid=(low+high)//2
#             if arr[mid]==query:
#                 return mid
#             elif arr[mid]<query:
#                 low=mid+1
#             else:
#                 high=mid-1
#     else:
#         return "list is not sorted"

#     return f'Item Not Found\nNew List = {insert_item(arr,low,query)}'

# print(BinarySearch([67,78,89,110,113],80))

# class Solution:
#     low=0
#     high=len(nums)-1
#     index=-1
#     def left(nums,target):
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 index=mid
#                 high=mid-1
#             elif nums[mid]<target:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return index

#     def right(nums,target):
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 index=mid
#                 low=mid+1
#             elif nums[mid]<target:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return index