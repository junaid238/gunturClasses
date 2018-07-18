# # # arith logical comparision
# # docstring in functions 
# # docstring --> desciption of what a function does 
# # syntax:
# # ------
# # declared just after definition 
# # ''' <docstring> '''
# # docstring --> __doc__

# # print( <function_name>.__doc__)

# # def addNums(a,b):
# # 	''' this adds two numbers ''' # ---> docstring just after he definition
# # 	sumn = a+b
# # 	print(sumn)
# # addNums(10,20)
# # print(addNums.__doc__)

# def printOptions():
# 	''' 1. Arithmetic
# 		2. Logical
# 		3. Comparision '''
# 	category = int(input("Enter the category you need "))
# 	return category
# def arith():
# 	''' 1. Addition
# 		2. Subtraction
# 		3. Multiplication
# 		4. Division
# 		'''
# 	option = int(input("Enter the operation you need"))
# 	return option
# def logical():
# 	''' 1. and
# 		2. or
# 		3. not
# 		'''
# 	option = int(input("Enter the operation you need"))
# 	return option
# def comparision():
# 	''' 1. Greater 
# 		2. lesser
# 		3. equal
# 		4. not equal
# 		'''
# 	option = int(input("Enter the operation you need"))
# 	return option
# def addN():
# 	''' this function adds numbers '''
# 	a = int(input("enter the first number"))
# 	b = int(input("enter the second number"))
# 	print(a+b)
# def subN():
# 	''' this function diff numbers '''
# 	a = int(input("enter the first number"))
# 	b = int(input("enter the second number"))
# 	print(a-b)
# def mulN():
# 	''' this function multiply numbers '''
# 	a = int(input("enter the first number"))
# 	b = int(input("enter the second number"))
# 	print(a*b)
# def divN():
# 	''' this function divides numbers '''
# 	a = int(input("enter the first number"))
# 	b = int(input("enter the second number"))
# 	if ( b>0):
# 		print(a//b)
# 	else:
# 		print("no operation if b = 0 given")

# print(printOptions.__doc__)
# category = printOptions()
# if(category == 1):
# 	print(arith.__doc__)
# 	operation = arith()
# 	if(operation == 1):
# 		print(addN.__doc__)
# 		addN()
# 	elif(operation == 2):
# 		print(subN.__doc__)
# 		subN()
# 	elif(operation == 3):
# 		print(mulN.__doc__)
# 		mulN()
# 	elif(operation == 4):
# 		print(divN.__doc__)
# 		divN()
# 	else:
# 		print("wrong input")
# elif(category == 2):
# 	print(logical.__doc__)
# 	logical()
# elif(category == 3):
# 	print(comparision.__doc__)
# 	comparision()
# else:
# 	print("Wrong input")




# passing list as an arguement to a function 

# def avgList(a):
# 	print(a)

# my = [1,2,3,4,5]
# avgList(my)
# myList = []
# def genList(length):
# 	for i in range(0,length):
# 		ele = input("enter the element")
# 		appender(ele)

# def appender(element):
# 	myList.append(element)
# 	print(myList)

# length = int(input("Enter the length of list you need"))
# genList(length)

