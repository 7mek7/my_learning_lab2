# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:21:38 2023

@author: 10
"""
# it show string leter 
x = 'abcdefghijk'
print(x[1:4])
print('==========')  

# it show from 2nd letter to -4 from last letter
x = 'abcdefghijk'
print(x[1:-4])

print('==========')

#it show from last letter to first
x = 'abcdefghijk'
print(x[::-1])

print('==========')

a = 'erfan' 
print(len(a)) # it show length of srtring
print(max(a)) # it show maximum letter of string
print(min(a)) # it show minimum letter of string

print('==========')

#ascii code
print(ord('a')) # it show ascii coode of (a or ....)
print(chr(97)) # this  is ascii code wich show carecter like 97 = a

print('==========')

s = 'python'
print('th' in s) #it show is ther that letter in our varrieble
print('th' not in s) #it show is ther that letter not in our varrieble
print(s == 'python') # it show (s or ...) = varrible

print('==========')

#if ther is number in string you can finde it with (isalnum)
s= 'python34'
print(s.isalnum()) # if ther is number in our varrible you can undrstand with tis code
#cheak some thing is number or not
d = '123'
print(d.isdigit()) # if our varrible is only number this code print (true)

print('==========')
# mohasebe adad yek reshte
a = '12a3bcd4'
k = 0
for ch in a :
    if ch.isdigit() == True:
        k += int(ch)
        
print(k) 

print('==========')

s = 'welcom to python'
print(s.startswith('we'))   
print(s.endswith('thon'))   

print(s.find('o'))           
print(s.index('o'))          

print(s.find('f'))           
#print(s.index('f'))          


print(s.find('o',5))        
print(s.find('o',10))       

print(s.count('o'))         
print(s.count('o',5))       

s = 'erfan@ut.ac.ir'
i = s.find ('@')
print(s[i+1:])              



s = 'welcom to python'
print(s.capitalize())     
print(s.title())          
     

        
        
        
        



















