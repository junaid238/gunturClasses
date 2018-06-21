# Python -- Sets , Dictionary Comprehensions -- Online - 21/06/2018
# ------------------------------------------------------------------

# d = {}
# dictin = {k1 : v1 , k2:v2}
# Comprehensions
# --------------
# sq = {1:1 , 2:4 , 3:9 , 4:16}

# sq = {x:str(x**2) for x in range(1 , 10) }
# print(sq)

# dlbd = {x:x*2 for x in range(1 , 10) }
# print(dlbd)

# dname = dict(zip(l1,l2))

# Sets and frozen sets 
# --------------------
# sets from 2.2 version of python
# ----
# --> collection
# --> can be iterated 
# --> not indexed
# --> not sliced
# --> storage only 
# --> mutbale ( modify , adding , removing )
# --> unique storage collections
# --> represented / comapred with maths sets 

# Syntax
# ------
# numsSet = {1,2 ,3 ,4,5,56}
# namesSet = {"khan" , "suma" , "surya" , "vamsi ", "sasi"}

# # type(numsSet) --> < class set >
# print(numsSet)
# print(type(numsSet))
# print(namesSet)
# print(type(namesSet))

# empty set cannot be declared as follows --> dictionary
# emptySet = {}
# print(emptySet)
# print(type(emptySet))

# operational empty set 
# empSet = set()
# print(empSet)
# print(type(empSet))

# # {} can be replaced with set((<elements>))
# numbers = set((1,2,3,4,5))
# print(numbers)
# print(type(numbers))

# indexing is not possible for sets 
# print(numbers[3])

# slicing is not possible for sets
# print(numbers[0:3])

# iterate over a for loop
# for i in numbers:
# 	print(i)

# set removes repetitions from the elements
# repNums = {1,2,3,4,5,67,8,9,1,2,3,9} # removes 1 2 3 9
# print(repNums)

# l1 = [1,2,3,4,6,8,9,0,8,6,5,4,30,2,2,4,56,8,9]
# # unique list --> in , not in
# print(l1)
# # converting to set to get only unique elements	
# l2 = set(l1)
# print(l2)
# # type casting back to list with unique elements
# l1 = list(l2)
# print(l1)

# Mutable properties
# ==================

# adding at last --> add(< element >) 
# removing from start --> pop()
# removing --> discard(< element >) , remove(< element >)
# concat --> ??
# copy --> copy()
# cleared --> clear()

# adding elements to numbers set
# numbers.add(10)
# print(numbers)
# numbers.add(100)
# print(numbers)

# removing an element from first from numbers set
# numbers.pop()
# print(numbers)

# removing a particular element from numbers set (5)
# numbers.remove(5)
# print(numbers)

# error removing a non existnig particular element from numbers set (5)
# numbers.remove(50)
# print(numbers)

# using diacrd removing a particular element from numbers set (5)
# numbers.discard(3)
# print(numbers)

# no error if discard is used removing a non existnig particular element from numbers set (5)

# numbers.discard(30)
# print(numbers)


# Math sets 
# ---------
# union()
# intersection()
# difference()
# subset()
# superset()


# a , b

# union --> all of a and b
# intersection --> common of a and b
# difference a b --> in a not in b
# difference b a --> in b not in a


# a.union(b)
# a.intersection(b)
# a.difference(b)
# a.subset(b)
# a.superset(b)


# namesSet = {"khan" , "suma" , "surya" ,  3 , "vamsi ", "sasi"}
# allset = {"surya" , "vamsi ", 1 ,3 ,56}
# un = namesSet.union(allset)
# print(un)
# ints = namesSet.intersection(allset)
# print(ints)
# diffA = namesSet.difference(allset)
# print(diffA)

# diffB = allset.difference(namesSet)
# print(diffB)

# namesSet.union(allset) --> namesSet | allset
# namesSet.intersection(allset) --> namesSet & allset
# namesSet.difference(allset) --> namesSet - allset
# allset.difference(namesSet) --> allset - namesSet

# namesSet.issubset(allset) --> allset < namesSet
# namesSet.issuperset(allset) --> allset > namesSet

# print(namesSet | allset)
# print(namesSet & allset)
# print(namesSet - allset)
# print(allset - namesSet)
# print(namesSet > allset)
# print(namesSet < allset)


# Frozen sets 
# ------------
# immutable version of sets
# type --> <class 'frozenset'>


# fNumsSet = frozenset((1,2,3,4,5,6))
# print(fNumsSet)
# print(type(fNumsSet))

# no adding of elements
# fNumsSet.add(90)
# print(fNumsSet)

# no removing of elements
# fNumsSet.remove(90)
# print(fNumsSet)

# setone = {1,2,3,4,5,6,7}
# setTwo = {4,5,7,9,10,11}

# common --> 4 , 5 ,7  ---> intersection
# all --> 1,2,3,4,5,6,7,9,10,11 --> union
# only setone --> 1,2,3,6 --> setone difference setTwo
# only setTwo --> 9,10,11 --> setTwo difference setone

# print(setone | setTwo)
# print(setone & setTwo)
# print(setone - setTwo)
# print(setTwo - setone)