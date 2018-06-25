# Python -- Functions -- online -- 25/06/2018
# -------------------------------------------
# Collections 
# Functions --> ?? , ?? , ??

# Function
# --------
# --> code snippet (lines of code) 
# --> one task 
# --> two types
# 	--> attribute fetching Functions
# 	--> parameterised Functions

# --> return type.  parameters
# 		0             0
# 		1			  1
# 		0 			  1
# 		1			  0 

# --> components of Function
# 		-> definition / declaration (once)
# 		-> implementation / business logic (once)
# 		-> call (multiple times)

# syntax 
# ------

# def func_name(): --> definition / declaration
# 	_____ |
# 	_____ |--> implementation
# 	_____ |

# func_name() --> Function call 

# call --> output 
# func_name --> identifier

# demo Functions
# --------------
# defining printme
# def printme():
	# implementing a print stmt to print Hello 
	# print("Hello ")
# making a call to printme Function
# printme()

#defining an mtfunct
# def mtfunct():

# # no implementation in the mtfunct
# 	pass
# # passing of pass statement to overcome not implementation
# # call to an mtfunct
# mtfunct()
# mtfunct()
# mtfunct()
# mtfunct()


# multiple calls
# --------------
# def printme():
# 	print("Hello ")
# # multiple calls to printme Function
# printme()
# printme()
# printme()
# printme()
# printme()
# printme()

# def printme():
# 	print("Hai ")

# printme()
# printme()

# two / multiple Functions --> same name  --> output -->latest function

# parameters
# ----------

# input(parameter) --> function --> output(call)

# --> formal parameter
# --> actual parameter

# call              --> def             --> impl --> output
# actual parameter  --> formal parameter--> impl --> output

#definition --> a --> formal parameter
# def printnum(b): # b =300
# 	print(b , " you entered") # b = 300 
# 	print(b+1)
# 300 --> actual parameter --> call is having it 
# b -> empty
# printnum(300) # --> b is 300 and 301
# b -> empty 
# printnum(500) # --> b is 500 and 501
# b -> empty 

# definition with multiple parameters
# def addNums(a,b):
# 	ans = a+b
# 	print(a  , " from a ")
# 	print(b  , " from b ")
# 	print(ans)
# # call with multiple parameters
# addNums(10,20)

# types of parameters
# -------------------
# 1 -> positional 
# 2 -> default
# 3 -> variable
# 4 -> keyworded


# task 
# ----
# functions --> aritmetic --> 2 numbers
# 			--> logical --> 2 numbers
