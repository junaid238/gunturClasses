# Python -- 1/08/2018
# -------------------
# Random
# - pseudo random number generation module 
# - numbers and collections only 
# - functions 
# - import random 
# - internal module with import 

# - book keeping
# - random numbers
# - collections sampling 
# - distributions ( normal , log , exponential , beta . . .)

# import random
# random for numbers
# ------------------
# random() --> generates a random float number b/w 0 and 1 
# <moduleRandom>.<randomFunction>()
# print(random.random())

# randrange(<start> , <end>) --> random integer b/w start and end both inclusive
# print(random.randrange(2,30))

# randint(<start> , <end>) --> random integer b/w start and end both inclusive
# print(random.randint(2,30))

# uniform(<start> , <end>) --> random float b/w start and end both inclusive
# print(random.uniform(2,30))

# random for collections
# ----------------------
# l1 = [x for x in range(2,25)] # list comprehensions 
# print(l1)

# random.shuffle(<collection>) --> shuffle all elements of a collection
# random.shuffle(l1)
# print(l1)

# random.choice(<collection>) --> generate one element from the collection
# print(random.choice(l1))

# random.sample(<collection> , k = <population>) --> generate k items from a collection
# print(random.sample(l1,2))

# choices() ---> ???

# c:/> python randomtask.py 4
# 3871
# c:/> python randomtask.py 3 6
# 387
# dkfkda

# import random as r
# import sys 

# def numMake(n): # system args and passing to n
# 	nums = ""
# 	for i in range(0,n): # iterating over n times
# 		nums = nums + str(r.randrange(0,9)) # concat
# 	print(nums)

# def chrMake(n):
# 	chrs = ""
# 	for i in range(0,n):
# 		chrs = chrs + chr(r.randrange(97,122)) # ASCII + concat
# 	print(chrs)

# if len(sys.argv) == 2:
# 	numMake(int(sys.argv[1]))
# elif len(sys.argv) == 3:
# 	numMake(int(sys.argv[1]))
# 	chrMake(int(sys.argv[2]))

c:/> python pwd.py "khan"
7865sdfv8765vcfx
c:/> python pwd.py "ravi"
4566vcdf3478ghvb
c:/> python pwd.py "khan"
user already exists

file
----
khan -- 7865sdfv8765vcfx
ravi -- 4566vcdf3478ghvb

dictionary 
----------
keys = names , values = passwords

Classes and objects --> 2/8/2018 
-------------------

