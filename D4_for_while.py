"""
Loop:
    for
    while
"""
#for
for i in range(4):
    print(i , end = ' ') 

print('\n ==============')    

for i in range(3,8):
    print(i , end= ' ')      
    
    
print('\n ==============')    

for j in range(5,10,2):
    print(j , end = ' ' )

print('\n ==============')    

s = 'erfan'
for ch in s:
    print(ch)
    
print('\n ==============')    

for _ in range(3):
    print('hello')

print('\n ==============')   
 
for i in range(9,2,-3)    :
     print(i , end=' ' )      

print('\n ==============')    
     
word = 'python'    
c = 0 
for i in word:
    c+=1
print(c)

print('\n ==============')    

word = 'ali'    
c = 0 
for i in word:
    if i =='a':
        c+=1
print(c)                


print('\n ==============')    

name = 'erfan'
v = 'aeiou'
c = 0
for ch in name:
    if ch in  v:
        print(ch)     
        c += 1
        
print(c)             

print('\n ==============')    

name = 'erfan'
v = 'aeiou'
a = [ch for ch in name if ch in v]
print(a)            

print('\n ==============')    

for i in range(1,4):
    for j in range(2,4):
        print(j,end=' ')
    print()
        
print('\n ==============')    

for i in range(1,4):
    for j in range(2,4):
        print(i,end=' ')
    print()


       
print('\n ==============')    

for i in range(2,5):
    for j in range(i):
        print(j,end=' ')
    print()

print('\n ==============')    

for i in range(2,5):
    for j in range(1,i):
        print(j , end = ' ')
    print()        

    
#break    

for i in range(5):
    if i == 3 :
        break
    else:
        print(i,end=' ') 


#continue 

for i in range(5):
    if i == 3 :
        continue
    else:
        print(i,end=' ')   

print('\n ==============')    
for n in range(10,15):
    for i in range(2,n):
        if n % i == 0 :
            print(n , end = ' ')
            break
        
print('\n ==============')    
for i in range(3,8):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i , end = ' ')
        
print('\n ==============')    
#while
      
i = 1      
while i<= 3:
    print(i , end= ' ')    
    i += 1
    
print('\n ==============')    


















    