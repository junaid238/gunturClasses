# Python 23-05-2018 Online --> strings part -2 
# Strings 
# -------
# index 
# slicing 
# immutable ---> cannot change 


# String concat 
# String operations
# string formating

# concatenation
# -------------
# adding of 2 or more things 
# not arothmetic addition 

# name = "Khan"
# tech = "python"
# name = name + tech 

# o/p
# ==
# Khan Python
# name + tech ---> conacat ( + )

# num = 100 
# name = "khan"

# num , name --> 100khan ( , )

# Type casting 
# ------------
# int --> str str()
# str --> int int()
# int --> float float()
# float --> int int()


# a = 100 
# < class int >

# a = str(a)
# < class str > ---> "100"

# name + num --> "khan" + 100
# error

# name + str(num) --> "khan" + "100"
# khan100

# c = "1000"
# < class str > --> string

# c = int(c)
# < class int > --> integer



# d = "Hyd" --> not base 10 
# < class str > --> string

# d = int(d)
# < class int > --> integer --> error -> ValueError: invalid literal for int() with base 10: 'Hyd'

# ASCII value ???

# character --> numerical value --> ASCII value 

# Char --> ASCII --> ord()
# ASCII --> Char --> chr()

# myname = "H"
# acii = ord(myname)


# raw strings 
# -----------
# unicode strings --> r&d 
# ---------------
# print("c:\programs\files\new\code\test") --> i/p
# c:\programs\files\new\code\test   -->expected o/p
# c:\programs
#            iles ---> real output 
# ew\code	est

# --> paths  , urls 

# print("c:\programs\\files\\new\code\\test")
# c:\programs\files\new\code\test

# path = r"c:\programs\files\new\code\test"


# print(100)
# print(10)
# print("python")
# print(str(100) + str(10) + "python")

# 100 
# 10 
# python
# end = '' --> 3.x --> XXXX 2.x XXXX
# print(100 , end = "")
# print(10 , end = "")
# print("python")
# 100 10 python

'''
comments 
--------
stop the execution 
single line --> 

# --> comment 

all these
are 
comments 

'''
# a = '''fbufbr
# rjbfjrblg
# jnnlgn
# rbfnlr
# '''

# String literals formating
# ---------------
# %d --> int
# %s --> string
# %f --> float
# only print()

# Syntax
# ------

# print(" %s %d %d %s %d " %("khan" , 100 , 20 , "python" , 35))
# username = "khan"
# marks = 20

# print("%s has got %d marks " %(username , marks))

# khan has got 20 % marks

# print("%s has got %d %% marks " %(username , marks))

# membership operators
# fancy formating--> 3 module 
# print("e" in "end")
# print("Py" in "Python")
# print("z" in "Khan")
# print("y" not in "Khan")

# identity operators --> is --> =
# tech = "python"
# print(tech is "python") # "python" is "python"
# print(tech is not  "Devops")
# print(tech is "py")
