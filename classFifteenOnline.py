# Python  --- Dictionaries Methods -- 20/06/2018 -- online
# ---------------------------------------------------------
# Dictionaries --> keys nd values

# key and value --> item 

formData = {"name" : "khan" , "age" :28 , "gender" :"M"}
# type(formData) --> dict
# formData["name"] --> khan
# print(formData , " from formData")
# print(type(formData))
# print(formData["name"]) # access value using key 
# print(formData["gender"])

# formData["name"] ="ravi" # modify the value using key 
# print(formData)

# formData["mobile"] = "987654321" # adding a key and value 
# print(formData)

# Operations 
# ----------
# removing a item
# --------------- 

# del 
# delete an item from Dictionary --> using key
# del formData["name"] --> name and khan
# del formData["name"]
# print(formData)

# pop()
# remove an item from Dictionary --> using key
# <dictname>.pop(<key>) --> key and value gets removed
# formData.pop("name") # remove name and khan
# print(formData)

# popitem()
# remove an arbitary item from Dictionary
# mostly last item --> anyitem 
# <dictname>.popitem() --> no inputs
# formData.popitem()
# print(formData)

# clear()
# clear all items from dictionary --> empty Dictionary
# <dictname>.clear()
# formData.clear()
# print(formData)

# len()
# no of items in a Dictionary
# len(<dictname>)
# print(len(formData))# --> 3

# copy()
# copy all items from one Dictionary to the other
# <new dict name > = <dictname>.copy()
# copiedDict = formData.copy()
# print(copiedDict)

# update()
# extend in lists 
# club items of two Dictionaries
# <dictOne>.update(<dictTwo>)
# all items of dictTwo get into dictOne
# <dictTwo>.update(<dictOne>)
# all items of dictOne get into dictTwo
# print("Before updating")
# print(formData , " from formData")
# employee = {"role" : "Lead" , "salary" : 10}
# print(employee , " from employee")

# # updated two Dictionaries
# formData.update(employee)

# print("After updating")
# print(formData , " from formData")
# print(employee , " from employee")

# .items() --> iterable 
# list of tuples of key value pairs 
# <dictname>.items()
# print(formData.items())
# for i in formData.items():
# 	print(i)

# .keys()  --> iterable 
# list of keys
# <dictname>.keys()
# print(formData.keys())
# for i in formData.keys():
# 	print(i)

# .values()--> iterable 
# list of values 
# <dictname>.values()
# print(formData.values())
# for i in formData.values():
# 	print(i)

# make a dictionary using two lists 
# ---------------------------------
# one list --> keys 
# other list --> values 

# len(one list) = len ( two list)
# if != 
# dict of min length list would be made
# len(dict) = len(min list)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = ["khan" , "suma" , "surya" , "asif" , "vamsi" , "sasi"]

# zip() --> convert 2 lists to a zip object
# zip(<listone> , <listtwo>)

# dict() --> zip object to Dictionary
# dict(zip(<listone> , <listtwo>))

# a = zip(l1,l2) # convert into zip object 
# print(a)
# # a --> zip object
# b = dict(a) # convert to dictionary
# print(b)

# c = dict(zip(l1,l2))
# print(c)

# Task 1
# ------
# enter len of Dictionary
# 2
# enter a key 
# "name"
# enter a value 
# "khan"

# enter a key 
# "age"
# enter a value 
# "28"
# {"name" : "value" , "age" :28}

# Task 2
# ------
# python demofile.py "khan"
# khan exists in dictionary

# python demofile.py "raghav"
# raghav does not exists in dictionary

# dictionary comprehensions 
# sets 