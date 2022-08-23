# -*- coding: utf-8 -*-
"""
Lecture 1. Introduction to python
"""

# =============================================================================
# A. Lists
# Lists are the most flexible structure to save or contain data elements.
# It comports any values
# 
# Importants operations:
    # Define with brackets []
    # Access values with positions from 0 to infinite: list[0:10]
    # Delete values with "del list[0:10]"
    # Remove values by position with "object.remove(0)"
# =============================================================================

names=["Qing", "Françoise", "Raúl", "Bjork","Marie","Paulo","Flavia"]
ages=[32,33,28,30,29,53,49]
country=["China", "Senegal", "España", "Norway","Brasil","Peru","Brasil"]
education=["Bach", "Bach", "Master", "PhD","PhD","Master","PhD"]

# Accessing
# Keep in mind the positions in Python start in 0.
names[0]

# several, using slices:
ages[1:-1] # second to before last

# several, using slices:
ages[:-2] # all but two last ones

# non consecutive
from operator import itemgetter # import function 'itemgetter' from operator package
list(itemgetter(0,2,3)(ages))

# difficul to understand?
ages[0:4:2] + [ages[3]] # Part1: from 0 to 4 pull 2 positions

# by position
country[2]="Spain"

# list changed:
country

# by value
country=["PR China" if x == "China" else x for x in country]
# Comprehension is important! Read step by step
# for every value in x (for x in country) 
# if x has "China" (if x == "China") write "PR China"
# list changed:
country

# by position
del country[-1] #last value

# list changed:
country

# by position
names.pop() #last value by default

# list changed:
names

# only 'del' works for several positions

lista=[1,2,3,4,5,6]
del lista[1:3]

#now:
lista

# by value
ages.remove(29) 
# list changed:
ages # just first ocurrence of value!!

# by value
education.remove('PhD') 

# list changed:
education # just first ocurrence!!

# deleting every  value:

lista=[1,'a',45,'b','a']
lista=[x for x in lista if x!='a']

# you get:
lista

# at the end
lista.append("abc")
lista

# PART ONE:
# first delete a position
education.pop(2)
education

# PART TWO:
# now insert in that position
education.insert(2,"Master")
education

# =============================================================================
# B. TUPLES
# Tuples are inmutable structures in Python
# They are usal for variables like ID passport, days, time, names etc.
# they look like lists but do not share much of their functionality:
    # We define with parenthesis ()
    # We can't use many of functions that we use in lists
# =============================================================================

# new list:
weekend=("Friday", "Saturday", "Sunday")
weekend[0]

# Python itself uses tuples as output of some important functions:

    # Concatenate names with ages
zip(names,ages) # Py return: Ok, I done that at 0x24a58478780.

# The zip functions creates tuples, by combining in parallel. You can see it if you turn the result into a list:
list(zip(names,ages))  # a list of tuples

# =============================================================================
# C. DICTIONARIES
# Dictionaries are like lists in R
# Dicts work in a more sophisticated way, as they have a 'key':'value' structure:
    # We define with braces {}
    # We access object in dictionaires with brackets and quotation marks    
# =============================================================================

classroom={'student':names,'age':ages,'edu':education}
# see it:

classroom # a ordem by default é alfabética

classroom['student']

# Notice I created a dictionary where the value is not ONE but a LIST of values.

# Once you access a value, you can modify it. You can also use pop or del using the keys. But you can not use append to add an element, you need update:

classroom.update({'country':country})
# now:
classroom

# =============================================================================
# D. DATA FRAMES
# Data frames are more complex containers of values. The most common analogy is a spreadsheet. To create a data frame, we need to call pandas:
# =============================================================================

import pandas

# We can prepare a data frame from a dictionary immediately, but ONLY if 
# you have the same amount of elements in each list representing a column.

# our data frame:
students=pandas.DataFrame(classroom)
## see it:
students

# But, let me update the dictionary with: 
names=["Qing", "Françoise", "Raúl", "Bjork","Marie"]
#
classroom.update({'student':names})
#
classroom

# In that case, you need this:
#then
students=pandas.DataFrame({key:pandas.Series(value) for key, value in classroom.items()})

# seeing it:
students

# Sometimes, Python users code like this:

import pandas as pd # renaming the library

students=pd.DataFrame({key:pd.Series(value) for key, value in classroom.items()})
students

# data of structure: list? tuple? dataframe?
type(students)

# type of data in data frame column
students.dtypes
# Quando temos ponto ao invés de parênteses significa que não estamos usando uma função, mas acessando os metadados do objeto
# dtypes é um metadado guardado no objeto students 

# details of data frame
students.info()

# number of rows and columns
students.shape 

# number of rows:
len(students)

# first rows
students.head(2) # compare with: students.tail(2)

# name of columns
students.columns

students.columns.to_list()# or simply: list(students)

students.age.to_list()# list(students.ages)

#one particular column
students.student

# or
students['student'] 

# it is not the same as: 
students[['student']] # a data frame, not a column (or series)

# this is also a DF
students[['country','student']]

# and this, using loc:
columnNames=['country','student']
students.loc[:,columnNames]

## Using positions is very common:
columnPositions=[1,3,0]
students.iloc[:,columnPositions] # iloc pede posições e loc pede nomes

students.iloc[4,1]=23 # change is immediate! (no warning)
students

studentsCopy=students.copy()
studentsCopy

# This is what you want get rid of:
byeColumns=['edu'] # you can delete more than one

#this is the result
studentsCopy.drop(columns=byeColumns)

studentsCopy

#NOW we do
studentsCopy.drop(columns=byeColumns,inplace=True)

#then:
studentsCopy

# axis 0 is delete by row
studentsCopy.drop(index=2,inplace=True) 
studentsCopy

studentsCopy.reset_index(drop=True,inplace=True)
studentsCopy