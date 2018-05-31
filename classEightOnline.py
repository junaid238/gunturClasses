# PYTHON --- Online -- 31-05-2018 -- Loops part 2
# -----------------------------------------------
# for -> numbers
# for -> strings
# string repetition
# -----------------

# print("a" * 10)
# print("python " * 3)


# skip execution of for --> pass statement
# for i in range(2,30):
# 	pass

# for loop --> inc 
# for loop --> dec --> range(end , start , -1 )

# for i in range(20,10,-1):
# 	print(i)
# Nested for loops:
# -----------------
# for :
# 	stmt1
# 	for :
# 		stmt2

# Patterns 
# --------
# code -->  (type 1)
# Patterns --> code ( type 2) 

# number Patterns
# ---------------
# 1
# 11
# 111
# 1111

# star Patterns
# -------------
# *
# **
# ***
# ****
# *****

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")


# print("*" * 1) # *
# print("*" * 2) # **
# print("*" * 3) # ***
# print("*" * 4) # ****
# print("*" * 5) # *****

# normal star pattern
# for i in range(1,6):
# 	print("*" * i)

# reverse star pattern
# for i in range(5 , 0 , -1):
# 	print("*" * i)

# first number pattern
# 1
# 11
# 111
# 1111
# 11111

# for i in range(1,6):
# 	print("1"*i)

# second number pattern
# 1
# 22
# 333
# 4444
# 55555
	 # i 	  i
# print(str(1) * 1)
# print(str(2) * 2)
# print(str(3) * 3)
# print(str(4) * 4)
# print(str(5) * 5)

# for i in range(1,6):
# 	print(str(i)* i)

# third number pattern
# 1
# 12
# 123
# 1234
# 12345

# 12345
# print("12345")
			 # 1. j
# for i in range(1,1):
# 	print(i , end="")
# print()
# for i in range(1,2):
# 	print(i , end="")
# print()
# for i in range(1,3):
# 	print(i , end="")
# print()
# for i in range(1,4):
# 	print(i , end="")
# print()
# for i in range(1,5):
# 	print(i , end="")
# print()
# for i in range(1,6):
# 	print(i , end="")

# for j in range(1,6):
# 	for i in range(1,j+1):
# 		print(i , end="")
# 	print()

# Prime - composite - classifier
# prime number --> 1 , number
# composite number --> more then 2 factors

# 12 --> composite --> 1 2 3 4 6 12 
# 13 --> prime --> 1 13

# count = 0.     count
# 12 % 1 == 0 --> 1
# 12 % 2 == 0 --> 2
# 12 % 3 == 0 --> 3
# 12 % 4 == 0 --> 4
# 12 % 5 == 2 
# 12 % 6 == 0 --> 5
# 12 % 7 == 5 
# 12 % 8 == 4 
# 12 % 9 == 3 
# 12 % 10 == 2 
# 12 % 11 == 1 
# 12 % 12 == 0 -> 6

# num = 12
# count = 0 
# for i in range(1,num+1):
# 	if num%i == 0:
# 		print(i , end =" ")
# 		count = count +1
# if count > 2:
# 	print("composite")
# else:
# 	print("prime")
# print(count)

# task on loops:
# --------------
# enter start number 3
# enter end limit 15

# 3 - prime
# 4 - composite
# 5 - prime
# 6 - composite
# 7 - prime
# .
# .
# .
# 14 - composite
# 15 - composite

# Task on loops 
# -------------
# 54321
# 4321
# 321
# 21
# 1