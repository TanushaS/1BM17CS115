n=int(input('Enter n'))
def fib(n):
    p=0
    q=1
    for i in range(n):
       r=p+q
       print(p,end="   ")
       p=q
       q=r
fib(n)
