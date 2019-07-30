# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:29:02 2019

@author: Sneha


Contain all the basic of Python 
1. List (any data inside a [] bracket is a list,include int,string,and float)
2. Slicing operation
3. Range Function
4. List
5. Nesting list


"""
#%% List as a  Data Structure

"Python List"

mylist1=[1,3,5,4,2]
mylist2=[1,4.2,'python',4.2]

print(mylist1)
print(mylist2)
print(type(mylist1))
print(type(mylist2))
#%% use of slicing operatore
a=[10,20,30,40,50,60,70,80]

print("a[2] =",a[2])
print("a[0:3] =",a[0:3])
print("a[5:] =",a[5:])

#%% range function
print(list(range(0,100)))

""" Range is gona create a memory object,
so it type caste it into List
do not use list as a variable name"""

#%% List are mutable
"""
it will not even strict on datatype , in place of
float value you can give string value as well"""

a=[10,20,30,40,50,60,70,80,90]
print(a)
a[3]=55.4
print(a)

#%% nested list or a Sub list

b=['spam',2.0,5,[10,"raj"]] 
print(b[3][1])
#%%  continating list | it will always perserve the order in which it is passed
c=a+b+[5,6]
c

#%% appending a single element

myList =[1,2]
i=1

while(i<=5):
    values=input("enter an element :")
    myList.append(values)
    i+=1
    print(myList)
    
#%% 
    """append - add single(one-one) element at a time
    extend - add multiple element at a time"""
    
myList1=[1,3,5,7,8]
myNewList=[1,2,3,4]

myList1.extend(myNewList)
print(myList1)
#%% insert function
""" extend and append add element at the end of the list
to add list or element in middle or at a particular place 
of a list we use insert function

insert function retain the element in the list
unlike replace function the element is being replaced

"""

list1=['a','d','b','c','d','e','f']
list1.insert(1,"$")
print(list1)
print(list1.index("d"))
#%%  Reverse function (simple reverse the element in the list , it will notsort or arrange in asc or desc) 

list1.reverse()
print(list1)

#%% Sort Function (default sort in ASC order)
"""in case of mix datatype sort will thrown error"""

list1.sort()
print(list1)

b=['spam',2.0,5,[10,'raj']]
b.sort() 

#%% del and remove
"""del--> when you know index position of the element we use del funciton
remove--> when you dont know the index position
"""
lst =[1,2,3,4,5,6,7,8,9,1]

del lst[4]
print(lst)

lst.remove(4)
print(lst)

print(lst)
del lst[1:3]
lst

#%% copy and clear function
#create an alias function , so any change in onel list will impact on other list as well

l1=[a,1,2,3]

l2=l1.copy()
l2

l1.clear()
l1

#%% Aggregate fuctions

num=[5,10,15,20,25,30]

print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))

#%% list and String
#TUPLES -is immutable (cannot modify) where else listwe can modify
x="python python"
#x=(1,2,3,4,5)
y=list(x)
z=tuple(x)
print(y)
type(y)
print(z)
type(z)
#%% zip function ()
a=[10,20,30,40,50,60]
b=[2,4,6,7,8]
c=[1,2,3,4,5,6]
print(list(zip(a,b,c)))










