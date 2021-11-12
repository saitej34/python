"""a,b=[int(x) for x in input("Enter two numbers: ").split(',')]
print("sum of {} and {} is {}".format(a,b,a+b))
print("subtraction of {} and {} is {}".format(a,b,a-b))
print("product is {} and {} is {}".format(a,b,a*b))
print("division of {} and {} is {}".format(a,b,a/b))
print("floor division of {} and {} is {}".format(a,b,a//b))
print("modulo of {} and {} is {}".format(a,b,a%b))
print("exponential of {} and {} is {} ".format(a,b,a**b))


a,b=[float(x) for x in input("Enter two numbers: ").split(',')]
print("sum of {} and {} is {}".format(a,b,a+b))
print("subtraction of {} and {} is {}".format(a,b,a-b))
print("product is {} and {} is {}".format(a,b,a*b))
print("division of {} and {} is {}".format(a,b,a/b))
print("floor division of {} and {} is {}".format(a,b,a//b))
print("modulo of {} and {} is {}".format(a,b,a%b))
print("exponential of {} and {} is {} ".format(a,b,a**b))

#implicit
a=int(input("Enter a int number: "))
b=float(input("Enter a floating number: "))
c=a+b
print("Type of a is ",type(a))
print("Type of b is ",type(b))
print("sum of a and b is ",c)
print("Type of c is ",type(c))



#explicit
a=int(input("enter a number: "))
b=input("Enter a string: ")
print("type of a: ",type(a))
print("type of b is ",type(b))
c=int(b)
print("type of c is ",type(c))
print("sum of a and c is ",a+c)


p=float(input("enter the principal : "))
t=int(input("Enter the number of years: "))
r=float(input("Enter the rate : "))
si=(p*t*r)/100
print("simple interest is ",si)
s=((1+r/100)**t)-1
ci=p*s
print("compoundinterest is ",ci)



#while

a=int(input("Enter a number: "))
i=0
while(i<=10):
    print("{}*{}={}\n".format(a,i,a*i))
    i=i+1


a,b,c=[int(x) for x in input("Enter three numbers: ").split(',')]
if(a>b):
    if(b>c):
        print("{} is largest".format(a))
else:
    if(b<c):
        print("{} is greater".format(c))
    else:
        print("{} is greater".format(b))

import math
a=int(input("Enter a number: "))
print("square root is ",(a**(1/2)))
print("square root is ",math.sqrt(a))


import math
while(1):
    a=int(input("Enter a number: "))
    if(a==99):
        break 
    elif(a<0):
        print("no square root value exists for negative nos")
        continue
    else:
        print("square root is ",(a**(1/2)))
        print("square root is ",math.sqrt(a))

k=1
n=int(input("enter n"))
for i in range(n):
    for j in range(i+1):
        print(k,end=' ')
        k=k+1
    print()


count=0
n=int(input("Enter a number: "))
while(n>=1):
    x=n%10
    count=count+1
    n=n/10
print(count)



n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if(i==j):
            print("$",end=' ')
        else:
            print("*",end=' ')
    print()

n=int(input("Enter n value: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(n,0,-1):
    for j in range(0,i,-1):
        print("*",end=' ')
    print()

import calendar
n=int(input("Enter a year: "))
y=calendar.calendar(n)
print(y)


def add(a,b):
    return a+b 
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b 
def prod(a,b):
    return a/b
while(1):
    a=int(input("Enter a value: "))
    b=int(input("Enter b value: "))
    print("select an operatio: 1.add\n2.sub\n3.mul\n4.prod")
    n=int(input())
    if(n==1):
        k=add(a,b)
        print(k)
    elif(n==2):
        k=sub(a,b)
        print(k)
    elif(n==3):
        k=mul(a,b)
        print(k)
    elif(n==4):
        k=prod(a,b)
        print(k)
    else:
        print("enter correct choice: ")

import time
start=time.time()
for i in range(10):
    print("AG")
end=time.time()
print("time taken is ",end-start)


a,b=[int(x) for x in input("Enter 2 numbers: ").split(',')]
k=lambda a,b:a*b
print(k(a,b))


import itertools,random
mydeck=list(itertools.product(range(1,14)),["spade","club","hearts","diamonds"])
random.shuffle(mydeck)
for i in range(5):
    print(mydeck[i][0],"of",mydeck[i][1])


rec=lambda n:rec(n/2)+1 if(n>1) else 1
n=int(input())
k=rec(50)
print(k)


import re

l=re.findall('/S+@/S+',s)
print(l)

lst=[1,2,3]
it=iter(lst)
for i in range(len(lst)):
    x=next(it)
    print(x*x)

d={'a':123,'s':234}
m=max(d.values())
mm=min(d.values())
print("the maximumois",m)
print("the min is ",mm)


"""

n=int(input("Enter the n value"))
for i in range(1,n+1):
    for j in range(1,i-1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
