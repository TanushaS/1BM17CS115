import random
import string
def genpwd():
  letters=string.ascii_letters+string.digits+"!@#$%^&*"
  length=random.randint(10,15)
  return ''.join(random.sample(letters,length))
flag=1
while flag:
   flag=int(input("Enter 1 to get a password or Enter 0 to exit:"))
   if flag==1:
     print(genpwd())
   else:
      flag=0   
