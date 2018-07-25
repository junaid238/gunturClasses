# Python -- file handling -- Online -- 25/07/2018
# -----------------------------------------------
# file --?? -- non volatile memory for storage of data --> ??

# program - list -> elements 
# run program - list will be empty 
# re run program - list will be empty 
# re run program - list will be empty 

# file --> data --> written --> always 
# run program - file will be empty --> data1  
# re run program - data1 + new data 

# Path mode operation 
# Path --> address of file --> /home/users/khan/python/tasks/filename.py
# mode --> what you want to do ?
# operation --> which mode  will work ?

# default --> .txt --> dont mention extension 
# file types			modules
# ----------          -------
# excel , csv  	--> pandas 
# excel        	--> xlsx
# csv files    	--> csv
# pdf files 		--> pypdf2


# modes (7) --> modes of file operation
# -------------------------------------
# read 			- r
# write 			- w
# append			- a
# read binary 	- rb 
# write binary 	- wb	
# read (update) 	- r+ , rb+
# write (update)	- w+ , wb+

# file --> open --> operate(modes) --> save (if required) --> close

# functions
# ---------
# open()	
	# - opening an existing file with a given mode 
	# - creating and opening a non existing file with a write mode 
# 	- return file object

# fileobject --> operations

# syntax
# ------
# <fileObject> = open(<"path + filename + extension"> , <"mode">)
# fo = open("/Users/junaid/Desktop/tuples.py" , "r")
# print(fo)
# fo.close()
# fobj = open("/Users/junaid/Desktop/page.html" , "w")
# fobj.close()

# with keyword
# 	-> indentation  
	# -> no need of closing

# syntax
# ------
# with open(<"path + filename + extension"> , <"mode">) as <fileObject>:

# with open("/Users/junaid/Desktop/pagewith.html" , "w") as fileobj:
# 	print("hey")

# writing to a file 
# -----------------
# write() --> single line to write
# writelines() --> multiple lines to write
# auto saved --> write , writelines
# open --> write 

# with open("/Users/junaid/Desktop/pagewith.txt" , "w") as fileobj:
# 	fileobj.write("first line\n")
# 	fileobj.write("second line")

# with open("/Users/junaid/Desktop/pagewith.txt" , "w") as fileo:
# 	fileo.write("third line\n")
# 	fileo.write("fourth line")

# with open("/Users/junaid/Desktop/pagewith.txt" , "a") as fileo:
# 	fileo.write("third line\n")
# 	fileo.write("fourth line")

# lines = ["first\n " ,"second\n " , "third\n " , "fourth\n"]
# lines = ("first\n " ,"second\n " , "third\n " , "fourth\n")

# foo = open("/Users/junaid/Desktop/pagewith.txt" , "w")
# foo.writelines(lines)

# one way 
# foo.write("first\n")
# foo.write("second\n")
# foo.write("third\n")
# foo.write("fourth\n")

#second way 
# for i in lines:
# 	foo.write(i)

# foo.close()

# reading the files --> ???