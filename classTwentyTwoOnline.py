# # modules and packages 
# module --> py file which can be executed 
# package --> folder which contains all python files


# myTasks (folder) --> one.py , two.py ,three.py (modules)

# myTasks --> package --> not a package

# myTasks --> one.py , two.py ,three.py , __init__.py

# __init__.py --> initialiser file 
# 			--> folder ===> package
# myTasks --> package

# syntax
# ------
# demo.py
# from <packageName> import <moduleName>
# 	<all module componenets>

# from myTasks import one

# from myTasks import classFourOnline
# from myTasks import classFiveOnline
# print(classFourOnline.a)


# Modules ( pre built and imported)
# -------
# random 
# os
# math

# random --> numbers and collections (lists,tuples,dictionaries)
# ------
# psedo random numbers 

# .random()
# 	---> a random float value b/w 0 and 1
# .shuffle()
# 	---> shuffle entire collection
# .choice()
# 	---> select a single random element from a collection
# .sample()
# 	---> select group of random elements from a collection
# .randrange()
# 	---> provide a random integer b/w start and end 
# .randint()
# 	---> provide a random integer b/w start and end 


import random as r 

print(r.random()) #0.2871267219811897











