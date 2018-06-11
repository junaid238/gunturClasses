# Python -- 11/06/2018 --- lists examples
# ---------------------------------------
# numsList = [34,78,98,9,76,13,19,7]
# print(numsList)

# Making a list dynamic entries from user
# ---------------------------------------
# fixed length --> len input -> 6
# elements of length --> 6 elements
# taking length of list
# length = int(input("enter length of list you need"))
# # making an empty list 
# nums = []
# # iterating for elements
# for i in range(0,length):
# 	element = input("enter the element")
# 	# adding elements to list
# 	nums.append(element)
# print(nums)

# l1 = [1,2,3,4,5,34,1,2,3,4,5,90]
# repeated = []
# unique = []
# for i in l1:
# 	if(i not in unique):
# 		unique.append(i)
# 	else:
# 		repeated.append(i)
# # print(1 in l1)
# # print(90 in l1)
# # unique = [1,2,3,4,5,34,90]
# print(unique)
# print(repeated)

# numbers = [20,30,12,23,45,90,50]
# doubles = []

# for i in numbers:
# 	doubles.append(i*2)

# print(doubles)
# allNums = []
# allEvens = []

# for i in range(2,30):
# 	allNums.append(i)
# 	# if(i%2 == 0):
	# 	allEvens.append(i)

# for i in allNums:
# 	if(i%2 == 0 ):
# 		allEvens.append(i)

# print(allNums)
# print(allEvens)


# List comprehensions 
# -------------------
# easy way of making lists --> adding elements , checking elements , operating on elements

# # empty list
# allNums = []
# # adding a range / limit
# for i in range(2,30):
# 	# adding elements to list
# 	allNums.append(i)
# print(allNums)
# syntax
# -------
# listName = [ <variable> <loop / limit>]
# allNums = [  i    for i in range(0,29)]
# print(allNums)

#making of empty list
# allEvens = []
# # giving limit or range
# for i in range(0,29):
# 	# checking using if 
# 	if (i%2 == 0):
# 		# adding elemets to list
# 		allEvens.append(i)
# print(allEvens)

# syntax
# ------
# listName = [<variable>   < loop / limit >   <condition>]
# allEvens = [ i  for i in range(0,29)  if (i%2 == 0)]

# print(allEvens)

#empty list declaration
# doubles = []
# # setting limit
# for i in range(0,20):
# 	# operation and adding an element to list
# 	doubles.append(i*2)
# print(doubles)

# syntax 
# ------
# listName = [<variable with operation>  <loop/limit> <condition>]
# doubles = [ i*2    for i in range(0,20) ]
# print(doubles)

# doublesOfEven = [ i*2    for i in range(0,20) if(i%2==0) ]
# print(doublesOfEven)

# Examples 
# --------
# l1 = [ i for i in range(12,40)]
# l2 = [ i for i in range(30,50) if(i%2 == 0)]

# print(l1)
# print(l2)

# # common elements ??? 
# common = []
# for i in l1:
# 	if (i in l2):
# 		common.append(i)
# print(common)

# Task 
# -----
# Enter a string 
# " iam in hyderabad for Python"
# vowels = [i ,a ,o ]
# repeatedLetters = [i , o , d , a]