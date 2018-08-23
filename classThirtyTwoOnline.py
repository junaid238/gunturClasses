# OOPS concepts 
# -------------
# 4 concepts --> objects 

# -> inheritance 
# 	- classes and objects 
# 	- acquiring of properties from one class to other class

# properties --> attributes (variables,methods)
# one class --> parent class , super class
# other class --> child class , sub class

# Types 
# -----
# -> single inheritance / simple inheritance
# -> multiple inheritance 
# -> multi level inheritance
# -> Hybrid inheritance

# java --> 15 and 17 (classes) , 16 (interfaces)lines 
# C++ --> 15 16 17 18 
# Python --> 15 16 17 18 (classes) 

# parent class --> p1 -->  10 vars and 5 methods 
# parent class --> p2 -->  10 vars and 5 methods 

# smiple inheritance  p1 --> c1
# ------------------
# child class --> c1 --> 10 vars and 5 methods <-- p1 inherited 
# 			--> 20 vars and 10 methods (15 P1 and 15 C1)


# multiple inheritance   p1 , p2 --> c2
# --------------------
# child class --> c2 --> 10 vars and 5 methods <-- p1,p2 inherited 
# 			--> 30 vars and 15 methods (15 P1 , 15 P2 and 15 C1)


# multi level inheritance  p1 --> c3 --> c4
# -----------------------
# child class --> c3 --> 10 vars and 5 methods <-- p1 inherited 
# 			--> 20 vars and 10 methods 
# 			--> using --> (15 vars and 7 methods)

# child class --> c4 --> 10 vars and 5 methods <-- c3 inherited
# 			--> 25 vars and 12 methods

# Hybrid inheritance
# ------------------
# p1 		p2 
# c1 		c2
# g1 		g2


# -> polymorphism 
# -> encapsulation 
# -> abstraction 




# 2.7 python --> all classes should inherit object class
# 3.x python --> all classes may inherit object class



# syntax:
# -------
# simple inheritance
# ------------------
# class <ParentClassName>:
# 	_______ parent attributes

# class <childClassName>(<ParentClassName>):
# 	_______ child attributes

# 	------- parent attributes

# multiple inheritance
# --------------------

# class <ParentClassName1>:
# 	_______ parent attributes 1

# class <ParentClassName2>:
# 	_______ parent attributes 2

# class <childClassName>(<ParentClassName1> , <ParentClassName2> ):
# 	_______ child attributes

# 	------- parent attributes 1
# 	------- parent attributes 2
# class parent(object): 2.7 convention

# class parent:
# 	name = "Python" # class variable
# 	def printMe(self , name): # instance method
# 		print(self) # printing object
# 		self.name = name # referencing with object 
# 		print("Hello " + self.name)

# class child(parent):
# 	address = "Hyderabad"
# 	def printAdd(self):
# 		print(self)
# 		print(" located at Hyderabad")

# print("from parent object")
# p = parent()
# print(p.name)
# p.printMe("khan")
# print("-----------------")
# print()
# print("from child object")
# c = child()
# print(c.address) # child attribute
# c.printAdd() # child attribute
# print(c.name) # parent attribute
# c.printMe("hari") # parent attribute
# print(child.__mro__) # tuple as output
# print(child.mro()) # list as output


# MRO ---> method resolution order
# child object --> parent method 
# 	--> same class 
# 	--> parent class 
# 	--> same module 
# 	--> pre defined libraries

# syntax
# ------
# <classname>.__mro__ --> mro variable
# <classname>.mro() --> mro method

# vehicle --> parent 

# 	no of wheels  
# 	current_speed

# 	start(speed)
# 	accelarate(speed)
# 	brake(speed)
# 	rev(speed)
# 	stop()
# 	printCurSpeed()

# car --> child 1 
# 	__init__()
# 	name 
# 	eng_cap 

# 	all from parent

# bike --> child 2
# 	__init__()
# 	name 
# 	eng_cap

# 	all variables
# 	not all methods (XXX rev XXX)

# b.start(20) --> print(b.current_speed) ==> 20
# b.accelarate(30) --> print(b.current_speed) ==> 50
# b.brake(15) --> print(b.current_speed) ==> 35