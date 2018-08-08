# Methods in classes (Python)
# Methods --> functions in classes 

# Types 
# -----
# class method 
# instance method 
# static method

class organisation:
	orgname = "DigitalLync" # class variable
	
	# making a default constructor
	# def __init__(self):
	# 	print("hello from constructor")

	# making a parameterised constructor
	def __init__(self , name):
		self.name = name
		print("hello "+self.name)

	def addNums(self,a,b): # self for storing object reference
		print(self)
		res = a+b
		print(res)

	# instance methods --> change with object
	def printName(self):
		# self.name = name # referencing name to self
		print("your name is " + self.name)
	
	# instance methods --> change with object
	def makeMail(self):
		self.mail = self.name + "@"+self.orgname + ".com"
		print("your mail is " + self.mail)

# emp1 object of organisation class
emp1 = organisation("khan") # object creation
emp1.printName()
emp1.makeMail()

emp2 = organisation("hari") # employee creation --> name
emp2.printName()
emp2.makeMail()

emp3 = organisation("ravi") # employee creation --> name
emp3.printName()
emp3.makeMail()


# emp1.printName("khan") # object reference for instance method
# emp1.makeMail() # object reference for instance method
# emp2.printName("ravi") # object reference for instance method
# emp2.makeMail() # object reference for instance method
# print(emp1.orgname) # object reference orgname
# print(organisation.orgname) # class reference orgname
# emp1 object calling addNums method
# emp1.addNums(10,20) 
# emp2.addNums(100,220) 

# emp1.addNums(10,20)  --> call --> method name , object reference , parameters
# keyword --> self 
# 	- stores object name referred 
# 	- it is the first formal parameter in a method 
# 	- it gets object name through call(method)
# java --> this 


# name --> khan
# email --> khan@DigitalLync.com

# constructor and destructor 
# --------------------------
# constructor --> default 
# 				parameterised 
# __init__() --> instance method 
# XXX object creation --> object XXX
# object creation --> call constructor --> constructor trigger class --> object 
# constructor call is made implicitly
# emp1=organisation()->__init__()->organisation->emp1->existence

# destructor --> delete the object
# 		- remove its existence
# 		- explicitly 	
# ---> ???		
# __del__() --> default destructor

# 9/8/18 --> types of methods

