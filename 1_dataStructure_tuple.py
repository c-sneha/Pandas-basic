# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:46:51 2019

@author: Sneha
"""
#            TUPLES

#mix datatype is supported
#denoted by () bracted 
# immutable | they cannot be changed
# sort doesnt work with tuple
# use when we have read only kinda data


#%%  
a=(5,'python',10+2j)
print(type(a))
print(a[0])

#%% Empty tuple
c=()
print(type(c))

c=tuple("Python") # taking each char out of string and tratingitas elemnet
print(c)

#%%
n_tuple =("mouse",[8,4,6],(1,2,3),8)
print(n_tuple[1])
print(n_tuple[1][2])

n_tuple[1][2]=9
print(n_tuple)

#n_tuple[2][1]=0

del n_tuple[1][2]
print(n_tuple)

del n_tuple
# will give error not define sprint(n_tuple)














