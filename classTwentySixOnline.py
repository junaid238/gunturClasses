# Python -- file handling -- part 2 -- 26/07/2018
# -----------------------------------------------
foo = open("/Users/junaid/Desktop/demo.txt" , "w+")
foo.write("hello\n")
foo.write("first\n")
foo.write("second\n")
foo.write("third\n")
foo.write("fourth\n")
foo.close()
# linux /mac -- UTF-8 
# windows -- cp1252

# reading of file content using Python
# ------------------------------------
# read()
# readline()
# readlines()

# read --> entire content on file from cursor position
# default --> cursor --> start
foo = open("/Users/junaid/Desktop/demo.txt" , "r")
# con = foo.read() # start to end 
# print(con)

# read(<count>) ---> print count no of chars
# con = foo.read(15) # start to 15 chars
# print(con)
# print("next read ")
# con2 = foo.read(10) # 16 to 26 chars 
# print(con2)
# print(foo.read()) # entire file from 27 th position

# readline() --> one line from cursor position --> start of cursor to \n
# first = foo.readline() # cursor = start of file 
# print(first) # start of second line
# second = foo.readline()
# print(second) # start = second line end = start of third line 

# readline(<count>)
# first = foo.readline(5) # count < no of chars in first line
# print(first)

# readlines() --> all the lines in a list with new line char

# linesList = foo.readlines()
# print(linesList)

# readlines(<count>) 
# (count <= no of chars in line) --> entire line 
# linesList = foo.readlines(7)
# print(linesList)

# tell() --> cursor current position 
# seek() --> move the cursor

# print(foo.read(10))
# print(foo.tell())
# print(foo.readline())
# print(foo.tell())

# c:/>python filename.py 7 
# 7 X 1 = 7 
# .
# .
# 7 X 10 = 70 

# sum = __  (0+1+2+3 . . .+7)
# avg = 4

Directories and OS module --> 27/07/2018


