# Python -- os module , random module
# -----------------------------------
# - pre defined modules
# - imported explicitly for use 

# files --> open , read , write and close 
# directories --> os module 

# os -- dependent -- directory /folder 
# - directory
# - paths 

import os 
# print(os.name) # posix
# current working path / folder  --> os.getcwd()
# print(os.getcwd()) # pwd --> linux/mac
# change a directory in os  --> os.chdir(<newpath>)
# os.chdir("/Users/junaid/Downloads/")
# print(os.getcwd())

# make directories 
# ----------------
# os.mkdir(<newFolderName>) 
# create new empty directory in current location
# os.mkdir("demo")
# os.makedirs("Python/code/tasks/khan")
# create a tree of directories (empty) at current location

# remove directories
# ------------------
# os.rmdir("demo")
# remove empty directories from given location
# os.removedirs("Python/code/tasks/khan")
# remove only empty directories but a tree of empty directories
# remove directories with files / non empty directories --> SHUTIL module

# exist --> ??? directories 
# check --> create 
# check --> remove

# os.path
# -------
# - system paths 
# - path manipulations 
# os.path.<function>()

# print(os.path.abspath("Python/code/tasks/"))
# return entire absolute path given in the parameter

# os.path.split() --> line 58
# os.path.splitext() --> line 59
# khan/songs/ a.mp3
# 			b.mp3
# 			c.mp3
# 		XX  d.jpeg XX
# 			e.mp3

# get all files+extensions --> check using spliting(.)
# get only extensions --> work on files 

# print("using split")
# path , filename = os.path.split("/Users/junaid/Desktop/guntur/classOneOnline.txt")
# print(path)
# print(filename)

# ans = os.path.split("/Users/junaid/Desktop/guntur/classOneOnline.txt")
# print(ans)

# print("using splitext")
# path , ext = os.path.splitext("/Users/junaid/Desktop/guntur/classOneOnline.txt")
# print(path)
# print(ext)

# for -> iterate --> filenames --> List --> %s
# --> store path --> List
# --> store ext  --> other list

# os.path.join()

# IMPORTANT
# ---------
# os.walk()
# 	- path 
# 		- directory
# 			- inside directory
# 				- one more directory
# 					- ___
# 				- second directory	
# 					- ____
# 			- file --> end point
# 		- file --> end point


# 	- path
# 		- directory
# 			- files --> end point

# a = os.walk(r"/Users/junaid/Downloads/")

# for paths , dirs , files in a:
# 	print("paths")
# 	print(paths)

# 	print("directories")
# 	print(dirs)

# 	print("all files")
	# print(files)

rename() --> ???

zip file -> unzip the files 
dis.zip -->folder --> multiple files(txt,py,pdf,jpeg)
txt --> all txt files --> 1.txt , 2.txt
py --> all py files --> 1.py , 2.py
pdf --> all pdf files --> 1.pdf , 2.pdf
jpeg --> all images --> 1.jpeg , 2.jpeg





