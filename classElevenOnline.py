Python -- online --- 7/6/18 -- Lists Methods / operations
---------------------------------------------------------
Lists --> mutable , collections , class list

indexed and sliced concat

Operations on lists / functions 
-------------------------------
--> attribute fetching functions ( . / dot)
--> parameterised functions (something)

len() --> length of elements in a list = highest index + 1

nums = [1,2,3,89,5,67,78 , 5 ,6 ,3]

highest index -->9

len = 10
len(nums) ==> 10 --> parameterised Method

listName.count(element) ==> repeated in list --> attribute fetching + parameterised

nums.count(1) ==> 1
nums.count(3) ==> 2
nums.count(89)==> 1
nums.count(100) ==> 0
nums.count(7) ==> 0 
nums.count(<index value>) -- error
nums[9] --> 3
nums.count(nums[<index>]) --> work 

listName.index(element) --> parameterised and attribute fetching
nums.index(89) --> 3
nums.index(3) --> 2

Modifications / mutable
=======================
add an element at the end of list --> listName.append(element)
add an element at specific index --> listName.insert(index ,element)
removes the last element --> listName.pop()
remove a specific element --> listName.remove(element)

listName.sort()  --> list sorting asc --> numbers 
				 --> list sorting char --> strings
		 		 --> error --> numbers + strings


list1.extend(list2) ---> concat (conditions)

list1 = [1,2,3,4]
list2 = [10,20,30,40]

list3 = list1 + list2
print(list1 + list2) --> [1,2,3,4,10,20,30,40]

print(list1) --> 1 , 2 , 3 , 4 
print(list2) --> 10 , 20 , 30 , 40 
print(list3) --> 1,2,3,4,10,20,30,40

print(list1) --> 1 , 2 , 3 , 4 
print(list2) --> 10 , 20 , 30 , 40 

list1.extend(list2)
print(list1) --> 1,2,3,4,10,20,30,40
print(list2) --> 10 , 20 , 30 , 40 


list2.extend(list1)
print(list2) --> 1,2,3,4,10,20,30,40
print(list1) --> 10 , 20 , 30 , 40 


changing elements
=================
list1 = ['asif', 'khan', 'sasi', 'suma ', 'vamsi']
list1[2] = "shahrukhkhan"
print(list1) --> 'asif', 'khan', 'shahrukhkhan', 'suma ', 'vamsi'


task
====

listNamesNums = [1,3,4,5,'asif', 'khan', 'sasi',4,5,'asif', 'khan', 'suma ', 'vamsi']

unique = [1,3,4,5,'asif', 'khan', 'sasi', 'suma ', 'vamsi']













