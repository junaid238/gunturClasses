# Python 
# ------
# Types of methods --> 3

# class --> company 
# object --> employee

# instance method 
# 	- object reference
# 	- self -- parameter 
# 	- <object>.<inst_method>
# 	- affects only instance/object(employee)
# 	 -- hike to employee
# 	 -- change of employee name

# class method 
# 	- class reference and object reference
# 	- cls -- parameter
# 	- <class>.<cls_method>
# 	- <object>.<cls_method>
# 	- affects both class and unmodified objects
# 	- decorator --> @classmethod 
# 			- function -> extra functionality to immediate function
# 			- @classmethod
# 				def one():
# 					___
# 		-- change of company name
# 		-- declaring holiday 

# static method
# 	- object reference
# 	- no parameter --> XXX self , cls XXX
# 	- <object>.<static_method>
# 	- affects none 
# 	- implement logics 
# 	- decorator --> @staticmethod 
# 		-- calculate % of hike 
# 			2387549 --> 12 % --> calc()
# 		-- check holiday 



class company:
	cname = "DigitalLync"
	cadd = "Hyderabad"
	emp_count = 20

	def __init__(self, name , role , salary):
		self.name = name 
		self.role = role 
		self.salary = salary
		self.email = self.makemail(self.name)
		company.emp_count += 1
		# print(''' Name: %s
			# role : %s
			# email : %s'''%(self.name , self.role , self.email))

	def makemail(self,name):
		self.email = name + "@" + company.cname +".com"
		return self.email

	@classmethod
	def changeCname(cls,newname):
		cls.cname = newname
		print("company name has changed to "+newname)

	@staticmethod
	def calc(salary , perc):
		finalSal = salary + (salary * perc)
		# print(finalSal)
		return finalSal

	def hikeamt(self , perc):
		finalSal = self.calc(self.salary , perc) 
		self.salary = finalSal
		# print(self.salary)
		# return self.salary


	def empDetails(self):
		print("your name is " + self.name)
		print("your role is " + self.role)
		print("your email is " + self.email)
		print("your salary is " , self.salary)

e1 = company("khan" , "PD" , 1000)
e2 = company("hari" , "PD" , 2000)
e1.hikeamt(0.1)
e1.empDetails()
e2.empDetails()

# e1.calc(50000 , 0.1) # calculate salary

# print(e2.cname + " from e2 before change")
# e2.cname = "DL"
# print(e2.cname + " from e2 after change by e2")
# print(e1.cname+ " from e1 before change by company")
# company.changeCname("Lync")
# print(e1.cname+ " from e1 after change by company")
# print(company.cname+ " from company after change by company")
# print(e2.cname + " from e2 after  change by company")


compdetails ---> name address count list of names of employees
fire --> remove --> destructor 
fired_emps --> fired employees names
