Derived data types 
-------------------
collections
------------
lists
tuples
dictionaries 
--------------------------------------
Lists [ ]
-----
--> MUTABLE objects 
--> Iterable objects
--> collection
--> stores heterogenous elements 
--> indexed 
--> sliced 
--> concatenated
--> operated by using functions 
--> Nested lists are also possible
-------------------------
SYNTAX
------
nameOfList = [ <elements> ]
names = ["khan" , "suma" , "surya" , "asif"]
name of list     ---> names 
elements of list ---> "khan" , "suma" , "surya" , "asif"

nums = [1,2,3,4,5,6]
name of list     ---> nums 
elements of list ---> 1,2,3,4,5,6

store loads of data --> collective data ( names , salaries)

heterogenous list
-----------------
numsNames = ["khan" , 1 , 2 ,4 , "suma" , 7 , "asif" , 40]

nested lists
------------
listInList = [1 ,2 ,5, [3,4,7,8] , 9 ,10]
lsit = [[[[[2]]]]]

Type --> < class list >
print(type(nums)) --> < class list >

MUTABLE --> open for change , modification
--------------------------------------------

Indexing and slicing of list
-----------------------------
names = ["khan" , "suma" , "surya" , "asif"]
			0		1 		  2			3
names[0] --> "khan"
names[3] --> "asif"
names[5] --> error 

names[0:2] --> "khan" , "suma"
names[1:3] --> "suma" , "surya"
-----------------------------------
Iterable 
--------
for <dummy variable> in listName:
	-- implementation --

	  i	
names[0]
names[1]
names[2]
names[3]

for i in range(0,4):
	print(names[i])

for i in names:
	print(i)

for i in "khan":
	print(i)

i/p
nums = [1,2,3,4,5,6]

o/p
1 3 5 
			  0. 1. 2.    3.       4.  5
listInList = [1 ,2 ,5, [3,4,7,8] , 9 ,10]
listInList[0] --> 1
listInList[5] --> 10

listInList[4] --> [3,4,7,8]
listInList[4][0] --> 3
listInList[4][1] --> 4
listInList[4][2] --> 7
listInList[4][3] --> 8

i/p vs o/p
===========
lsit = [[[[[[3,4]]]]]]
>>> lsit[0][0][0][0][0]
[3, 4]
>>> lsit[0][0][0][0][0][0]
3
>>> lsit[0][0][0][0][0][1]
4

----------------------------------
concatenation of lists
----------------------
l1= [1,2,3,4,5]
l2= [4,5,7,8,9,10]
l1 + l2 
[1,2,3,4,5,4,5,7,8,9,10]
l3 = l1 + l2 
l3 ==> [1,2,3,4,5,4,5,7,8,9,10]
--------------------------------
operations on lists --> 7/6/18
-------------------


c:/>python listtask.py
enter a list
[1,2,3,4,5]
19

listofnums = [1,1,1,1,1,1]









