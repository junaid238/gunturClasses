# Python -- functions (part -2) -- online - 27-06-2018
# ----------------------------------------------------
# function 
# 	-- declaring 
# 	-- implementaion 
# 	-- call

# -> parameters ( 0 1 0 1)
# -> return type( 0 0 1 1)

# parameters --> inputs to a function --> ( )
# addNums(a,b) --> formal , actual parameters
# ----------------------------------------------

# Return type
# -----------
# input  --> parameters
# output --> return type --> keyword


# adding of two nums 
def addNums(a,b):
	ans = a+b
	# print("sum of nums " +str(ans))
	# define a return type
	return ans
# assigning a function call to "a"
a = addNums(10,200) # ans = 210 
print("from a " + str(a))

# # #subtracting of two nums 
# def subNums(c,d):
# 	diff = c-d
# 	print("difference of nums "+str(diff))
# subNums(addNums(200,300) , 100) # subNums(500 , 100)


# def addsub(a,b):
# 	add = a+b
# 	diff = a-b
# 	# return add/diff
# 	# returning add value
# 	# return add
# 	return str(add) + "  " + str(diff)
# a = addsub(20,10)
# print("from return "+str(a))


# add(20,40) # 60 # change in add effects all 
# sub(output of add , 10) # 50
# mul(output of sub , 10) # 500
# div(output of mul , 10) # 50

# def add(a , b):
# 	ans = a + b
# 	return ans 
# addRes = add( 20 , 50 )

# def sub(res , b):
# 	ans = res - b
# 	return ans
# subRes = sub(addRes , 10)

# def mul(res , b):
# 	ans = res * b
# 	return ans
# mulRes = mul( subRes , 10)

# def div(res , b):
# 	ans = res // b
# 	return ans
# divRes = div(mulRes , 10)

# print("from add function " , addRes)
# print("from sub function " ,subRes)
# print("from mul function " ,mulRes)
# print("from div function " ,divRes)

# Task 
# ----
# res = strVowel("Iam in Hyderabad")
# print(res)
# # I a i e a a 

# avg = avgNums(10,20,30,40)
# print(avg)
# # 25