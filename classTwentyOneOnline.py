# # Python -- modules and packages --- online -- 4/07/208
# # -----------------------------------------------------
# Module
# ------
# --> simple python file
# --> demo.py --> module 
# --> <filename>.py 

# Run a module
# ------------
# c:/>python <filename>.py

# Types:
# -----
# internal
# internal imported 
# external

# internal: all these are already in you module 

# -------------
# demo.py
# <internal>.py
# def addn(a,b):
# 	----
# 	----
# 	----
# print("a") --> a
# addn(10,20) ---> error --> addn is not existing in demo.py
# ---------------------------------------
# internal imported
# -----------------
# addNums.py

# sys --> module --> did not download XXX
# internal ---> imported 

# import sys  # importing sys module explicitly 
# c:/>python addNums.py 10 20 
# 30

# internal imported --> sys , os , math , cmath , datetime ....

# ------------------------------------------
# external modules:
# ----------------
# module --> unavailable in python installation
# module --> downloaded --> imported
# python , third party

# Numpy , pandas , plt , pillow , seaborn . . . . .
# import numpy --> error --> module not found

# download
# --------
# python package manager --> pip --> python packaging index
# windows --> default available 
# c:/>pip / pip3  
# ----
# ----
# ----
# ----
# ----
# ----
# ----
# ----
# ----
# ---> pip is installed

# c:/> pip / pip3  
# pip not installed

# linux , windows , mac: 
# ----------------------
# google --> get-pip.py file 
# bootstrap --> get-pip.py

# get-pip.py --> download (copy paste) and run 
# c:/>python get-pip.py
# c:/>pip / pip3 
# ----
# ----
# ----
# ----

# external modules --> ???

# pip install <package/module>

# c:/>pip install numpy
# c:/>pip install pandas
# c:/>pip install matplotlib

# python/installation/folders/./././site-packages

# numpy , pandas , matplotlib --> site-packages

# import numpy 
# import pandas
# import matplotlib

# pip commands
# -------------
# pip install <name> ---> install packages
# pip freeze --->  get lisk of packages with versions
# pip list --> get lisk of packages

# n dimensional array --> numpy
# list -> one dimensional array

# importing modules 
# -----------------
# import check.py XXXX
# import classTwentyOnline # valid 
# # all components of check module---> this file
# # <moduleName>.<module component>

# # accessing of function from module
# classTwentyOnline.addNum(10,20)  # valid
# # print(addNum(10,20)) # not valid
# print(classTwentyOnline.addNum(10,20))

# # accessing of variable from module
# print(classTwentyOnline.l2)


# aliasing
# --------
# import classTwentyOnline as cto # alias
# cto.addNum(10,20) 
# print(cto.addNum(10,20))
# print(cto.l2)

# specific import from a module
# ------------------------------

# from <module> import <component>

# from functools import reduce
# from classTwentyOnline import l2 , l3 , addNum
# print(l2)
# print(l3)
# print(addNum(10,20))

# package:
# --------
# folder with python files
# files 	---> folder ???
# 		---> package ???
# 	--> one.py
# 	--> two.py
# 	--> three.py




