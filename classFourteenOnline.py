# Python -- Dictionaries -- 19/06/2018 -- Online
# ----------------------------------------------
# Dictionary --> collection 
# -> heterogeneous collection
# -> arbitary 
# -> indexed 
# -> iterated
# -> mutable

# l1 = ["khan" , 28 , "M" , "Py" , "9876543210" , "address hyd "]
# l2 = ["ravi" , 28 , "M" , "Py"  , "address hyd "]

# l1[5] --> address
# l2[4] --> address

# 0 , 1 , 2 , 3 . . . . .n 

# l1[name] --> khan XXX l1[0] --> khan
# l2[name] --> ravi XXX l2[0] --> ravi

# Dictionary
# ----------
# indicies --> customised  -> name , age , gender , mobile  . . . . .n 
# elements --> customised  -> "ravi" , 28 , "M" , "Py", "address hyd "

# indices --> Dictionary --> keys 
# elements --> Dictionary --> values 
# key + value = item

# Syntax
# ------
# emptyDictionary = {}
# empDict = {key1 :  value1 , key2 : value2 , key3 : value3}

# keys --> unique , immutable [numbers , strings , tuples]
# values --> can be anything , repeated 

# type(<dictionaryname>) --> < class dict >


# Accessing elements of a Dictionary
# ----------------------------------
# indexing --> 

# dictName[key] --> value --> if key exists 
# dictName[key] --> if key doesnot exists --> anything 

# modifing an element
# -------------------
# dictName[key] = newValue --> modify oldvalue into newValue --> if key exists 

# dictName[key] = newValue --> add key and value to Dictionary --> if key doesnot exists


# delete a dictionary
# -------------------
# del dictionaryname --> entire dictionary 
# del dictName[key] --> the item with key 

# input vs output
# ---------------
# emp = {}
# >>> type(emp)
# <class 'dict'>

# employee = {"name" : "khan" , "age" : 28 , "mobiles" : ["9876" , "8765"]}
# >>> print(employee)
# {'name': 'khan', 'age': 28, 'mobiles': ['9876', '8765']}

# >>>employee["name"]
# 'khan'

# >>> employee["age"]
# 28

# >>> employee
# {'name': 'Ravi', 'age': 28}
# >>> employee["name"] = "Khan"
# >>> employee
# {'name': 'Khan', 'age': 28}

# >>> employee["mobile"] = "9876543210"
# >>> employee
# {'name': 'Khan', 'age': 28, 'mobile': '9876543210'}

# >>> del employee["name"]
# >>> employee
# {'age': 28, 'mobile': '9876543210'}

# >>> del employee
# >>> employee
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'employee' is not defined

# # Operations / methods in dictionary ---> 20/6




