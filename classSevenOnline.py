# PYTHON -- Online -- Looping structures -- 30 -05-2018
# -----------------------------------------------------
# Loops 
# -----
# --> repetitions 
# --> some logic 
# 3 things 
# --------
# condition / limit
# implementation / statement
# inc / dec
# ----------
# 3 uses
# ------
# -> numbers 
# -> strings
# -> collections 

# 2 types
# -------
# for loop
# while loop 


# Numbers with loop 
# -----------------
# Java -->for(i=0 , i<=10 , i++){
# 			print(i)
# 		}

# i=0 --> t --> print 0
# i=1 --> t --> print 1
# i=1 --> t --> print 1
# i=1 --> t --> print 1
# i=10 --> t --> print 10
# i=11 --> f --> exit of loop

# start -> initialisation ---> i = 0
# end -> limit --> i<=10
# implementation --> print(i)
# inc / dec --> inc --> i++

# range() function --> ONLY NUMBERS
# ================
# range(end)
# range(start , end)
# range(start , end , step)

# range(end) 					--> range(10) --> 0 1 2 3 4 5 6 7 8 9 
# range(start , end) 			--> range(4,10) --> 4 5 6 7 8 9
# range(start , end , step)	--> range(1,10,2) --> 1 3 5 7 9


# for + range() --> loops in python ( numbers )

# i --> dummy variable
# for i in range(11):
	# print(i)
# i is dead here 

# for i in range( 10 , 30 ):
# 	print(i , end =" ")

# for i in range(1 , 100 , 5):
# 	print(i)

# i = 0 --> i+1
# i = 1 --> i+1
# i = 2 --> i+1
# .
# .
# .
# .
# .
# i = 9 --> i+1
# i = 10 --> exit 

# print --> command --> 2.7
# print 10
# print(10)

# print --> function --> 3.6
# print(10)

# number = 200
# print("%d %d" %(1 , number))
# print(1 , number)

# print() --> new line --> automatic 
# print( , end = "") --> avoid new line --> 3.x version

# a = 10 
# b = 20
# print(a , end =" ")
# print(b) 

# for loops --> strings 
# ---------------------

tech = "Python"
# P --> tech[0]
# y --> tech[1]
# t --> tech[2]
# h --> tech[3]
# o --> tech[4]
# n --> tech[5]
# print(tech[0])
# print(tech[1])
# print(tech[2])
# print(tech[3])
# print(tech[4])
# print(tech[5])

# Other langauges 
# for i in range(0,len(tech)):
# 	print(tech[i])

# Python accessing chars directly
# for i in tech:
# 	print(i)

# acccessing chars in a variable
# name = "Khan"
# for x in name:
# 	print(x)
# acccessing chars from string without a variable
# for m in "Guntur and Hyderabad":
# 	print(m , end= " ")

# even and odd --> 1- 40
# 1 - odd
# 2 - even 
# 3 - odd
# 4 - even

# 39 - odd

# for i in range(1,40):
# 	if(i%2 == 0):
# 		print("%d - %s " %(i , "even"))
# 	else:
# 		print("%d - %s " %(i , "odd"))

# Task2 --> multiplication table 

# output
# ------
# enter the number 3
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27
# 3 X 10 = 30

