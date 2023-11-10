#3. Write a Python program to get the largest number from a list. 
# max=0
# mylist=[int(num) for num in input("enter the numbers in the list:").split()]
# for i in mylist:
#     if(i>max):
#         max=i

# print("the largest element in list is:",max)
##############################################

# n=int(input("enter the no. of elemets in list:"))
# mylist=[]

# for i in range(n):
#     num=int(input("enter a number:"))
#     mylist.append(num)
    
# if(len(mylist)==0):
#     print("list is empty")
# else:
#     max_num=max(mylist)
#     print("Max element in list is:",max_num)

#################################################################################################################################

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 
# x, y, z = 3, 4, 6
# array3d = [[['*' for _ in range(z)] for _ in range(y)] for _ in range(x)]

# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             print(array3d[i][j][k], end=' ')
#         print()  # Move to the next line for the next "y" dimension
#     print()  # Add an empty line to separate the "x" dimensions
############################################
# import numpy as np
# x,y,z=3,4,6

# array_3d=np.full((x,y,z),'*')
# print(array_3d)

##############################################################################################################################

#23. Write a Python program to flatten a shallow list. 
# def flat_list(listt):
#     flatlist=[]
#     for i in listt:
#         if isinstance (i,list):
#             flatlist.extend(flat_list(i))
#         else:
#             flatlist.append(i)
#     return flatlist

# shaw_list=[[2,44,67],[23,65,78,85],[21,12,5,221,75],8]

# final=flat_list(shaw_list)
# print(final)

###############################################################################################################################

#33. Write a Python program to generate all sublists of a list. 
# def sub_list(listt):
#     sublist=[]
#     for i in listt:
#         if isinstance (i,list):
#             print(i)


# multi_list=[[2,44,67],[23,65,78,85],[21,12,5,221,75],[2,3]]
# sub_list(multi_list)

################################################################################################################################

#43. Write a Python program to split a list into different variables. 
# mylist=[ int(num) for num in input("enter in list").split()]
# j=1
# for i in mylist:
    
#     print(f"var{j}=",i)
#     j+=1

################################################################################################################################

#53. Write a Python program to create a list with infinite elements. 
# mylist=[]
# while 1:
#     n=input("enter yor element:")
#     if(n=='*'):
#         break
#     else:
#         mylist.append(n)

# print(mylist)

###############################################################################################################################

#63. Write a Python program to insert a given string at the beginning of all items in a list. 
# mylist=[i for i in input("enter element in the list:").split()]
# print(mylist)
# n=input("enter a string to add in all the elements of list:")
# for j in mylist:
#     print(n+str(j))

################################################################################################################################

# #73. Write a Python program to remove consecutive duplicates of a given list. 
# #Original list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# #After removing consecutive duplicates: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]


# # Import the 'groupby' function from the 'itertools' module
# from itertools import groupby

# # Define a function 'compress' that takes a list of numbers 'l_nums' as input
# def compress(l_nums):
#     # Use 'groupby' to group consecutive duplicates and return the unique keys
#     return [key for key, group in groupby(l_nums)] 

# # Define a list 'n_list' with consecutive duplicate elements
# n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# # Print a message indicating the purpose of the following output
# print("Original list:") 

# # Print the original list 'n_list'
# print(n_list)

# # Print a message indicating the purpose of the following output
# print("\nAfter removing consecutive duplicates:")

# # Call the 'compress' function with 'n_list' as an argument and print the result with consecutive duplicates removed
# print(compress(n_list))
        
        
        

        

