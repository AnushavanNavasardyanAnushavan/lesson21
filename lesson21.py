# ---------------------------------Linear Search---------------
# def leneary_cearch(my_list, n, x):
#     for i in range(0, n):
#         if my_list[i] == x:
#             return i
#     return -1
# my_list = [2, 3, 4, 10, 40, 21]
# x = int(input("enter number --> "))
# n = len(my_list)
# res = leneary_cearch(my_list, n, x)
# if res == -1:
#     print("ellement is not present in list")
# else:
#     print("ellement is  present at index ", res)
# print(res)

# ----------------------------------------------------------------
# -------------------Binary Search----------------------------
# def binary_search(my_list, n, start, stop):
#     mid = (start + stop) // 2
#     if n == my_list[mid]:
#         return mid
#     elif n < my_list[mid]:
#         return binary_search(my_list, n, start, mid - 1)
#     else:
#         return binary_search(my_list, n, mid + 1, stop)
        

# my_list = [1, 2, 3, 5, 10, 15, 27, 34, 55, 78, 98]
# n = int(input("ENTER NUMBER ---> "))
# start = 0
# stop =len(my_list)
# print(binary_search(my_list, n, start, stop))




# ---------------------------------Bubble Sort -------------------------

# my_list = [10, 75, 43, 15, 25, -4, 27]

# def bubbleSort(my_list):
#     last_item = len(my_list) 
#     for i in range(0, len(my_list)):
#         for j in range(0, last_item - 1):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#     return my_list
# print("old list --> ", my_list)
# print("new list --> ", bubbleSort(my_list))


# ---------2-rd dzev-------------
# my_list = [10, 75, 43, 15, 25, -4, 27, 8, 2]
# for i in range(0, len(my_list) - 1):
#     for j in range(0, len(my_list) - i - 1):
#         if my_list[j] > my_list[j + 1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print(my_list)


# -------------------Binary Search----------------------------

# def bin(myList, n, start, stop):
#     if start > stop:
#         return False
#     else:
#         mid = (start + stop) // 2
#         if n == myList[mid]:
#             return mid
#         elif n < myList[mid]:
#             return bin(myList, n, start, mid - 1)
#         else:
#             return bin(myList, n, mid + 1, stop)

# myList = [1, 2, 3, 5, 6, 7, 8, 11, 15, 22]
# n = 5
# start = 0
# stop = len(myList)
# print(bin(myList, n, start, stop))



# ---------------------------------Bubble Sort -------------------------
# myList = [5, 4, 10, 3, 25, 22, -2]
# for i in range(0, len(myList) - 1):
#     for j in range(0, len(myList) - i  - 1):
#         if myList[j] > myList[j + 1]:
#             myList[j], myList[j + 1] = myList[j + 1], myList[j]
# print(myList)