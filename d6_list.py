# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 11:17:11 2023

@author: 10
"""

a = [4 , 6 , 8]
print(type(a)) # show type
print(len(a)) # show length

print('=========')

print(a.index(6)) # it show index(loc) of 6 or ...
print(a[1])

# we can change lists
a[1] = 10

# lists are ordered
b = [1 , 2]
c = [2 , 1]
print(b == c)

print('=========')

# for print list of names we can use (for)

friends = ['taha' , 'ali' , 'erfan']
for f in friends :
    print(f)
    
print('=========')
# list can have difrent carecter
L = ['ali' , 3 , 'erfan' , 2.5 , False]

print('=========')
# slising in list
a = [7 , 5 , 30 , 2 , 6 , 25]
print(a[1:4])
print(a[3: ])
print(a[ :3])
print(a[3:0])

print('=========')
#for make some thing *2
a = [2 , 7]
b = a*2
print(b)
print('=========')

# for colect 2 list

w = [1 , 2 , 3 , 4 , 5]
c = ['w' , 'e' , ' y']
r = w + c
print(r)

print('=========')
#for undrstand some thing in list  
j = [2 , 4 , False , 2.3 , 'w']
print(4 in j)
print(4 not in j)
print('=========')

# practice show max carecter
a = [7 , 5 , 30 , 2 , 6 , 25 ]
m = -1
for i in a:
    if i > m:
        m = i

print(m)

# for do it in esey way
print(max(a))

        







