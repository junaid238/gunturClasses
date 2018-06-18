# Tuples -- Python Online -- 18/06/2018
# -------------------------------------
# Tuple--? 
# -> collecttion 
# -> heterogeneous 
# -> indexed 
# -> sliced
# -> concat
# -> immutable 
# -> iterable 

# < class tuple >

# Syntax
# ------

# nameOfTuple = (< elements >)
# nameOfTuple = < elements > , 

# nums = (1,2,3,4,5) --> tuple 
# numsW = 1,2,3,4,5,  --> tuple 

# Accessing elements of tuple
# ---------------------------
# indices  --> 0 , 1 , 2 ....n

# [] --> Accessing
# () --> declaration

# namesTuple = ("khan" , "suma" , "asif" , "surya")
# namesTuple[2] --> asif  --> []
# namesTuple(2) --> error --> () --> function 

# slicing 
# -------
# namesTuple[0:2]
# namesTuple[start:end-1]

# concat
# ------
# tuple1 = (1,2,3)
# tuple2 = ("a" , "b" , "c")

# tuple2+tuple1 --> (1,2,3,"a" , "b" , "c")

# tuple3 = tuple2+tuple1
# tuple3 --> (1,2,3,"a" , "b" , "c")

# modify elements of tuple 
# ------------------------
# immutable data type 

# add XX
# remove XX 
# delete element XX

# delete entire tuple 
# index()

# Use cases
# ---------
# declare constants 
# pi = 3.14
# epsilon = 2.71
# mathConsts = (3.14 , 2.71)
# mathConsts[0] --> pi
# mathConsts[1] --> epsilon

# values --> dont change frequnetly 
# employee --> ( name , email , mobile )

# school fee --> 3 yrs
# fees = (10k , 20k , 30k ) --> 2018 , 2019 , 2020
# 2021 --> change fee  --> modify the tuple 
# 20k --> 24k 

# change elemets of tuple 
# -----------------------
# type casting 
# ------------
# tuple --> list --> modify --> tuple 

# tuple --> list ---> list()
# list --> tuple ---> tuple()

# tupl1 = ("khan" , "suma" , "asif" , "surya" , "preetham " , "vamsi")
# dummy = list(tupl1)
# dummy -->list 
# modify 
# tupl1 = tuple(dummy)
# tupl1 --> tuple 

# Tuple comprehensions
# --------------------
# XXX nothing XXX 

# Task -- Tuple
# -------------
# coll = [34,39,19,13 , [12,35,7] , (90,190), 120 , (100,200)]
# output = [34,39,19,13,12,35,7,90,190,120,100,200]

# form data --> job 
# -----------------
# 20 fields 
# name 
# email 
# mobile 
# qual
# per address
# pre address
# prevjob 
# .
# .
# .
# [] --> list 
# () --> tuple

# cand1
# candidate[5] --> per address
# candidate[6] --> prevjob

# cand2
# per address --> XXXX
# candidate[5] --> prevjob

# Dictionaries --> customise the indices  --> default
# named tuples --> modify the fields --> internal (special)

# Input vs output
# ===============
# >>> tupl1
# ('khan', 'suma', 'asif', 'prabhatsurya', 'preetham ', 'vamsi')

# >>> for i in tupl1:
#      	print(i)

# khan
# suma
# asif
# prabhatsurya
# preetham 
# vamsi

# >>> "khan" in tupl1
# True

# tupl1 = ("khan" , "suma" , "asif" , "surya" , "preetham " , "vamsi")
# >>> tupl1
# ('khan', 'suma', 'asif', 'surya', 'preetham ', 'vamsi')
# >>> dummy = list(tupl1)
# >>> type(dummy)
# <class 'list'>
# >>> dummy[3] = "prabhatsurya"
# >>> dummy
# ['khan', 'suma', 'asif', 'prabhatsurya', 'preetham ', 'vamsi']
# >>> tupl1 = tuple(dummy)
# >>> tupl1
# ('khan', 'suma', 'asif', 'prabhatsurya', 'preetham ', 'vamsi')














