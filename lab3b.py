import random
import string
def func1():
    chars1=string.ascii_uppercase
    chars2=string.ascii_lowercase
    chars3=string.digits
    chars4='!@#$%^&*'
    c=string.ascii_letters+string.digits+'!@#$%^&*'
    size=random.randint(10,15)
    p= "".join(random.choice(chars1)+random.choice(chars2)+random.choice(chars3)+random.choice(chars4))
    size-=4
    p+=''.join(random.choice(c) for j in range(size-1))
    return ''.join(random.sample(p,len(p)))
print("1.New password:")
print("2.Exit")
print("Enter your choice:")
ch=int(input())
while(ch==1):
    print("Password:",func1())
    print("Enter your choice:")
    ch=int(input())
    

