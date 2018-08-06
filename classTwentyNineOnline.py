# # # PYTHON -- classes and objects
# # # -----------------------------
# # # module - 4 
# # c++ or java --> class is mandatory 
# # python --> class is not mandatory

# # python --> oops --> object oriented programming structure 


# # class ---> ??
# # 	- collection  --> variables and functions 
# # 	- entities or attributes 
# # 	- functions in class --> methods
# # Average --> nums 
# # what am doing --> mean / avg --> function
# # where am i doing --> nums --> variables

# # 	- variables --> where yo do ?
# # 	- methods --> what you do ?
# # 	- blueprint of object 

# # blueprint --> framework --> paper plan to a building 
# # paper plan to a building --> home 
# # 		class 			 --> object

# # one class with one name 

# # object --> instance of class 
# # 		- real existence of class 
# # 		- real world entity 

# # single blueprint --> multiple homes 
# # XXXX multiple blueprints --> single home XXXX

# # single class --> multiple objects
# # XXX multiple classes --> single object XXX

# # object class --> primitive of all code in python

# # syntax of class
# # ---------------
# # class <className>: --> definition of a class
# # 	<implementation1>
# # 	<implementation2>
# # 	<implementation3> --> implementations of class
# # 	<implementation4>

# # syntax of object
# # ----------------
# # <objectName> = <className>()

# # function definition --> declaring class
# # function implementation --> implementation of class
# # function call --> object creation

# # call --> function  ---> output 
# # object --> class --> output
# # object ===> instantiate a class --> trigger 
# # doc string --> '''<immediately after defining''' 


# class nums:
# 	''' demo class for example ''' # docstring of nums class 
# 	a = 10 # class variables
# 	b = "hai" # class variables

# numsObj = nums()
# # print(numsObj)
# secondObj = nums()
# # print(secondObj)
# # print(type(numsObj))
# # print(type(secondObj))

# # -> attributes, entity 
# # 	-> references ( . )
# # 		- class reference --> <className> . <entity>
# # 		- object reference --> <object> . <entity>

# # print(nums.a) # - class reference
# # print(nums.b) # - class reference
# # print("------------")
# # print(numsObj.a) # - object reference
# # print(numsObj.b) # - object reference

# numsObj.a = 20 
# print(numsObj.a)
# # print(nums.a)
# nums.a = 300
# print(numsObj.a) 
# print(nums.a)
# print(secondObj.a)

# class values --> class reference and object reference
# a =10
# class.a -> 10
# obj1.a -> 10 
# obj2.a -> 10 

# object values --> obj1.a = 20 --> will ONLY change in obj1 memory
# class.a -> 10
# obj1.a -> 20
# obj2.a -> 10

# class change of value --> class.a = 300
# 		--> change for class and unchanged objects

# class.a -> 300
# obj1.a -> 20
# obj2.a -> 300

constructors and destructors --> 7/8/2018
