# Python class - 2 Online 21-05-2018

# Python -- uses 
# features , introduction 

# main compenents in Python programming 
# -------------------------------------

# Keywords and identifers
# -----------------------
# library of words (Keywords)
# 	pre defined
# 	cannot be changed 
# 	should only purpose defined 
# 	cannot be deleted 
# Python 2.7 --> 31 Keywords
# Python 3.6 --> 33 Keywords
# mostly small case --> None , True , False

# get keywords
# ------------
# import keyword 
# keyword.kwlist

# identifers
# ----------
# library of words given by user/developer
# names of compenents(datatypes , functions , classes , objects , files )
# rules 
# 	cannot use keyword
# 	start with letter
# 	cannot start with number or special char
# 	start with small case ( recommended )
# 	can start with an underscore ( _ , __)(special)
# Input - output 
# --------------
# > a = 10 ALLOWED
# >>> 1 = "khan" not ALLOWED
#   File "<stdin>", line 1
# SyntaxError: can't assign to literal
# >>> 1name = "Python" not ALLOWED
#   File "<stdin>", line 1
#     1name = "Python"
#         ^
# SyntaxError: invalid syntax
# >>> name = "Python" ALLOWED
# >>> NAME = "Python" ALLOWED but not recommended
# >>> @name = "Python" not ALLOWED
#   File "<stdin>", line 1
#     @name = "Python"
#           ^
# SyntaxError: invalid syntax
# >>> name@ = "python" not ALLOWED
#   File "<stdin>", line 1
#     name@ = "python"
#           ^
# SyntaxError: invalid syntax
# >>> _name = "python" ALLOWED but special case
# >>> __name = "python" ALLOWED but special case
# ----------------------------------------------
# Variable 
# --------
# -> mini bucket to store values / data
# 	-> name (identifier)
# 	-> data ( many types)
# 	-> memory location ( address where it is stored )
# -> var_name = < value >

# -> datatypes--> type(var_name)
# -> memory --> id(var_name)

# var_name --> identifier
# value --> data 
# = -> assignment operator 
# ---------------------------------------------
# Data Types 
# ----------
# 5 datatypes 
# 	2 independent --> numbers , Strings 
# 	3 derived --> lists , tuples and dictionaries 

# Numbers --> integer , float , long , complex 
# int class
# maximum possible integer in python

# import sys 
# sys.maxint --> python 2.7
# sys.maxsize --> python 3.6
# 9223372036854775807

# a = 100 
# a --> name 
# 100 --> value stored in a 
# datatype --> 100 --> int
# id(a) --> memory location
# type(a) --> datatype


# >>> a = 198.89
# >>> type(a)
# <class 'float'>

# >>> n = 9+8j
# >>> type(n)
# <class 'complex'>



# Operations 
# ----------
# 6 operators
# --> arithmetic 
# --> logical 
# --> comparision
# --> bitwise 
# --> membership ( no numbers )
# --> identity  ( no numbers )

# a = 100 
# b = 8

# arithmetic operators
# + , - , * , / , // , %  , **

# print("sum of a and b " , a+b)
# print("difference of a and b " , a-b)
# print("product of a and b " , a*b)
# print("quotient of a and b " , a/b)
# print("real quotient of a and b " , a//b)
# print("remainder of a and b " , a%b)
# print("power/ exponent of a and b " , a**b)
# Output 
# ======
# sum of a and b  108
# difference of a and b  92
# product of a and b  800
# quotient of a and b  12.5
# real quotient of a and b  12
# remainder of a and b  4
# power/ exponent of a and b  10000000000000000

# logical operators  --> T / F 
# -----------------
# logical and --> and --> T / F 
# logical or --> or  --> T / F 
# logical not --> not  --> T / F 

# a 		b 		and 		or
# T 		T 		 T 			T
# T 		F 		 F 			T
# F 		T 		 F 			T
# F 		F 		 F 			F


# a   not(a)
# t     f
# f     t


# comparision operators --> T / F 
# -------------------------
# > , < , >= , <= , == , !=  --> T / F 
# a = 25
# b = 30
# c = 25 
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a!=b)
# print(c==a)
# print(c==b)

# print( a<b and b==c)
# T and F
# print( a<b or b==c)
# # T or F 
# a = 10 # 00001010
# b = 20 # 00010100
# a&b =    00000000 -> 0
# a|b =    00011110 -> 30

# Bitwise operators
# -----------------
# bitwise and  -> &
# bitwise or  -> |
# bitwise not -> ~ 2's complement operator

# print(a&b)
# print(a|b)
# print(~a)
# 64 32 16 8 4 2 1
# 	0 0 0 1 0 1 0 
# ~x = -(x+1)
# ~10 = -(10+1)=-11
# ~21 = -(21+1)= -22
# print(~21)
