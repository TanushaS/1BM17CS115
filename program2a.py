def find(l,num):
   if num in l:
      return True
   else:
      return False
l=list(map(int,input('Enter the list of elements').split()))
n=int(input('Enter the number to be searched'))
print(find(l,n))         
