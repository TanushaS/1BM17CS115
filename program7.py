def check_prime(i):
  flag=1
  if i > 1:  
    for j in range(2,i):  
       if (i%j) == 0:  
           flag=0 
    if flag:  
       f1.write(str(i)+'\n')

def check_happyNumber(i):    
    rem = sum = 0   
        
    while(i > 0):    
        rem = i%10   
        sum = sum + (rem*rem)    
        i = i//10
    return sum  
def happy(i):          
  result = i    
     
  while(result != 1 and result != 4):    
    result = check_happyNumber(result)    
  if(result == 1):    
    f2.write(str(i)+'\n')      
  elif(result == 4):    
    pass       
              
f1=open('One.txt','w')
f2=open('Two.txt','w')
for i in range(1,1001):
     check_prime(i)  
for i in range(1,1001):
     happy(i)   
f1.close()
f2.close()
f1=open('One.txt','r')
f2=open('Two.txt','r')
content1=f1.readlines()
content2=f2.readlines()
flag=1
for i in content1:
    if i in content2:
        print(i,end='  ')
        flag=0
if flag:
    print('\nNO OVERLAPPING OF NUMBERS')            
f1.close()
f2.close()
