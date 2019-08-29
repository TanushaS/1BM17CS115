def reverse1(s):
   l=s.split()
   l.reverse()
   for i in l:
      print(i,end=' ')
   print()   
def reverse2(s):
   l=s.split()
   for i in l:
     print(i[-1::-1],end=' ')
   print()     
s=input('Enter the string')  
reverse1(s)
reverse2(s) 
