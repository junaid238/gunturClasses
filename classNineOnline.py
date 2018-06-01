# PYTHON -- ONline -- 1/06/2018 --- Loops part 3
# -----------------------------------------------
# for --> nested 
# patterns  -> number and string 

#Prime composite between a limit
# taking a start point
# s = int(input("enter a start number"))
# # taking a end point
# e = int(input("enter a end number"))
# # iterating b/w start and end 
# for i in range(s , e+1):
# 	count = 0
# 	# between 1 and i= 4
# 	for j in range(1,i+1): # 1 1 , 1 2 , 1 3 , 1 4 
# 		if i%j == 0 :
# 			count += 1
# 	if count > 2:
# 		print(" %d is a %s number" %(i , "composite"))
# 	else:
# 		print(" %d is a %s number" %(i , "prime"))
# 	# reinitialising to previos state
# 	count = 0

# While loop
# ----------
# -> initialisation 
# -> limit / condition 
# -> statement / implementation ( pass )

# SYNTAX
# < initialisation >
# while < condition >:
# 	< implementation > / pass
# 	< inc / dec >
	
# condition --> t --> execute --> implementation
# condition --> f --> exit execution

# print 1 - 9 using while inc 

# a = 0 # initialisation
# while a<10: # condition
# 	print(a) # implementation
# 	a += 1 # inc /dec

# print 9 - 1 using while dec 
# b = 10 # range(9,0,-1)--> for 
# while b>0:
# 	print(b)
# 	b -= 1 # b = b-1 

# infinite loop --> mostly while 
# using condition always true 
# a = 10 
# while a == 10:
# 	print("hai")

# using True keyword
# while True:
	# print("hello")
	# pass

# Control statements:
# -------------------
# keywords 
# pass
# 	-->overcome non implemented blocks ( ifelse , for , while , method , class)
# break 
# 	--> only for loops 
# 	--> condition --> stop the loop
# continue
# 	--> only for loops 
# 	--> condition --> pauses the loop
# 	--> next statements

# pass statement
# for i in range(0,12):
# 	pass

# break statement
# for i in range(0,12):
# 	print(i , end = " ")
# 	if i == 6:
# 		break
# print()
# for i in range(0,12):
# 	if i == 6:
# 		break
# 	print(i, end = " ")

# i = 0 --> 0
# i = 1 --> 1
# i = 2 --> 2
# i = 3 --> 3
# i = 4 --> 4
# i = 5 --> 5
# i = 6 --> 6 break

# break for numbers using for loop 
# tech = "qwertyuioplkjhgfdsazxcvbnm"
# for i in tech:
# 	print(i)
# 	if i == "p":
# 		break

# continue with for 
# for i in range(0,12):
# 	if i == 6:
# 		continue # stop for 6 and then continue
# 	print(i)
# continue with while 
# a = 0
# while a<10:
# 	a += 1
# 	if a == 6:
# 		continue # skips 6 from printing 
# 	print(a)
	
# continue with string and for 
# tech = "Python and Data Sceinces"
# for i in tech:
# 	if i == "a":
# 		continue
# 	print(i , end ="")

# task 
# ----
# *
# **
# hello # 3
# ****
# *****
# hello # 6
# *******
# ********
# hello # 9

# 1
# 22
# 333
# 4444
# ***** # 5
# 666666
# 7777777
# 88888888
# 999999999
# ********** # 10
