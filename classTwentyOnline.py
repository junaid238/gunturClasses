# Python -- functions -- lambda functions  -- online -- 2 -07-2018
# ---------------------------------------------------------
# Map Filter and Reduce functions

# Function - snippet of code
# 		- single task (output)
# 		- return type --> outcome
# 		- parameters --> input
# parameters
# 	- 4 types
# 	- positional
# 	- default 
# 	- variable ( extension to positional ) 
# 	- keyworded ( extension to default )

# tasks 
# -----
# 1 --> category 
# 2 --> operation 
# 3 --> numbers 
# 4 --> output ( return type ) 

# lambda functions( lambda operator  / anonymous functions )
# -----------------------------------
# definition  + implementation  --> single line
# call

def addNum(a,b):
	res = a+b # implementation = operation
	return res # does not count as implementation

# ans = addNum(10,20)
# print(ans)


# re write addNum function using lambda
# syntax
# ------
# IMP auto returned -->lambda
# <funct_name> = lambda formalparameters : operation
# <funct_name> = lambda formalparameters : implementation
# <funct_name>(<actual parameters>) # call

#definition 		# implementation
# addNum = lambda a,b : a+b
# function call to addNum
# print(addNum(10,20))
# print(addNum(100,200))

# sqrd = lambda a : a**2
# print(sqrd(20))
# print(sqrd(50))

# map , filter and  reduce
# ------------------------
# collections ( lists )

# l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]

l3 = [11,22,33,44,55]

# l4 = [1,4,9,16,25] # squares of l1

# associative squaring
# def listSq(l1):
# 	l4 = []
# 	for i in l1:
# 		l4.append(i**2)
# 	return l4

# print(listSq(l1))


# map -> associative operations
# print(l1)
# print(l2)

# syntax:
# -------
# <mapobject> = map(<functionName> , lists/list)

# map(<functionName> , lists/list) ---> map object

# <listName> = list(map(<functionName> , lists/list))

# returns map object
# l3 = map(lambda a,b : a+b , l1 ,l2)

# associative sum of elements from 2 lists
# type casted to list
# l3 = list(map(lambda a,b : a+b , l1 ,l2))
# print(l3)

# associative squares from 1 list
# sqList = list(map(lambda x:x**2 , l1))
# print(sqList)


# filter --> associative checking
# if else --> ??? --> T/F

# returning list of even / odd by checking
# def evenChk(l1):
# 	l5 = []
# 	for i in l1:
# 		if i%2 != 0:
# 			l5.append(i)
# 	return l5
# print(evenChk(l1))

# syntax:
# ------
# <listName> = list(filter(<funct_name> , list))

# l5 = list(filter(lambda x:x%2 == 0 , l1))
# print(l5)

# list comprehensions for generation of list 
# numsList = [x for x in range(2,40)] 
# print(numsList)
# checking for multiples of 5 using filter
# mulfive = list(filter(lambda x:  x%3 == 0  ,numsList))
# print(mulfive)

# reduce ---> cumulative operation 

# sum of all elements in list --> cumulative
# def sumEle(l1):
	# res = 0
# 	for i in l1:
# 		res += i
# 	return res
# print(sumEle(l1))

# [1,2,3,4,5] --> 15 
# reduce --> not default available 
# import it from python libraries

# syntax:
# -------
# <listName> = reduce(<funct_name> , list)

# from functools import reduce

# # cumulative addition of list elements
# sumAll = reduce(lambda x,y :x+y , l1)
# print(sumAll)

# # cumulative multiplication of list elements
# mulAll = reduce(lambda x,y :x*y , l1)
# print(mulAll)

# task
# -----
# lambda , map , filter  --> dictionaries