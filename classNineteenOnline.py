# Python -- function paramaters -- online -- 28-06-2018
# -----------------------------------------------------
# function --> single task 
# 	- paramater
# 	- return type 

# paramaters
# 	- positional ( noof args in definition = no of args in call)
# 	- default (customised args in call and values in definition)
# 	- variable (multiple args 0 - n) --> tuple
# 	- keyworded (multiple args 0 - n) --> dictionary


# def addNums(a,b):
# 	sum = a+b
# 	return sum

# a = addNums(100,200)
# print(a)

# positional arguements/paramaters
# def avgNums(a,b,c):
# 	print("a" , a , "b" , b , "c" , c)
# 	avg = (a+b+c)//3
# 	print(avg)
# avgNums(10,30,20) # valid 
# avgNums(10,20) # not valid
# avgNums(10,20,30,40) # not valid

#default arguements/paramaters

# cake shop -- cakes 
# fla = "vannila" , wei = "2kgs" , sha = "square"
# cust1 --> vannila , 2kg , round ( 3 inputs )
# cust2 --> chocolate , rectangle , 1kg ( 3 inputs )
# cust3 --> pineapple , 3kg ( 2 inputs ) square
# cust4 --> 5kg ( 1 input ) vannila and square
# cust5 --> cake ( no inputs ) vannila 2kgs square


# issue at third function call missing sha as positional arguements
# def makeCake(fla , wei , sha):
# 	print("you have ordered "+fla + " flavoreded cake of "+wei+ " kgs and "+sha+" shape")
# makeCake(fla = "vannila" , wei = "2" , sha = "round")
# makeCake(fla = "chocolate" , sha = "rectangle" , wei = "1")
# makeCake(fla = "pineapple" , wei = "3")


#default arguements/paramaters
# def makeCake(fla = "vannila" , wei = "2" , sha = "square"):
# 	print("you have ordered "+fla + " flavoreded cake of "+wei+ " kgs and "+sha+" shape")

# makeCake(fla = "vannila" , wei = "2" , sha = "round")
# makeCake(fla = "chocolate" , sha = "rectangle" , wei = "1")
# makeCake(fla = "pineapple" , wei = "3") # automatically sha = "square"
# makeCake(wei = "5") # automatically sha = "square" fla ="vannila"
# makeCake() # automatically fla = "vannila" , wei = "2" , sha = "square")

# variable paramaters / arguements
# find avg of 3 numbers
# def avgNums(a,b,c):
# 	print("a" , a , "b" , b , "c" , c)
# 	avg = (a+b+c)//3
# 	print(avg)
# avgNums(12,15,90)
# # find avg of 4 numbers
# def avgNums(a,b,c,d):
# 	print("a" , a , "b" , b , "c" , c)
# 	avg = (a+b+c+d)//3
# 	print(avg)
# avgNums(12,15,90,100)
# avgNums(12,15,90) # invalid
# avgNums(12,15) #invalid

# variable paramaters (0 paramaters to n paramaters)
# args ---> tuple --> arguements from the call 
# convention --> *args , *vars

# def VavgNums(*args):
# 	# print(args)
# 	# print(type(args))
# 	sum = 0 
# 	for i in args: # args = 10,20,30,40
# 		sum = sum + i
# 	# print(sum)
# 	avg = sum // len(args)
# 	print(avg)

# VavgNums(10,20) # valid
# VavgNums(10,20,30) # valid
# VavgNums(10,20,30,40) # valid
# VavgNums(10,20,30,40,50) # valid

# positional + variable arguements/paramaters
# def VPavgNums(a , b , *args): # *vars *abc *varibales
# 	print("args" ,args)
# 	print("a" ,a)
# 	print("b" ,b)

# 	# print(type(args))
# 	sum = a + b 
# 	for i in args: # args = 10,20,30,40
# 		sum = sum + i
# 	# print(sum)
# 	if (len(args) == 0 ):
# 		avg = sum // 2
# 	else:
# 		avg = sum // (len(args) + 2 )
# 	print("avg" , avg)
# VPavgNums() # division with zero eliminate 
# VPavgNums(10) # non sense eliminate
# VPavgNums(10,20) # valid
# VPavgNums(10,20,30) # valid
# VPavgNums(10,20,30,40) # valid
# VPavgNums(10,20,30,40,50) # valid

# keyworded arguements/paramaters
# dictionaries --> key and values
# toppings = "almonds" ---> key = toppings , value = "almonds"
# **kwargs , **kwvars , **abcds , **wern --> definition

# def makeCake(fla = "vannila" , wei = "2" , sha = "square" , **kwargs):
# 	print(kwargs)
# 	print(type(kwargs))
# 	print("you have ordered "+fla + " flavored cake of "+wei+ " kgs and "+sha+" shape")

# makeCake(fla = "vannila" , wei = "2" , sha = "round")
# # toppings --> almonds 
# makeCake(fla = "vannila" , wei = "2" , sha = "round" , toppings = "almonds")

task 1
------
python myProg.py
1. arith
2. logical
3. comparision
enter your input 1

1. add
2. sub
3. mul
4. div
enter your input 1   /	2

enter a num 10 
enter a num 100
110    / 	-90

task 2
------
c:/>python listfunc.py
enter len of list 
4
enter the element
10
enter the element
20
enter the element
30
enter the element
40

your list is 
[10,20,30,40]
1. mean
2. median
3. sum
enter your input 1
25
enter your input 2
25
enter your input 3
100






