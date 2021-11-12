"""lst=[1,2,3,4,"sai,'v"]
print(lst)
#list is collection of the dissimilar datattypes in which values seperated with commas,enclosed by squarebraces
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[2:5])
print(list[:9])
print(list[::3])
print(list[1:9:3])

l=[1,2,3,4,5,6,7,8,9]
print(l[0])
l[0]=500
print(l[0])  #lists are mutable i.e they canbe changed
print(l)


lst=[1,2,3,4,5,6]
print(lst)
lst.append(500)  #append function inserts element at last
print(lst)
del lst[6]      #del list[index deletes elemnt
print(lst)


lst=[1,2,3,4,5,6]
del lst[0:3]
print(lst)

lst=[1,4,5,6]
lst1=[2,3]
lst[1]=lst1
print(lst) 


lst=[1,2,3,4,5,6]
del lst[:]
print(lst)

#BASIC LIST OPERATIONS


lst=[1,2,3,4,5,6]
print(len(lst))
lst2=[7,8,9]
lst=lst+lst2  # list concat
print(lst)
l=[1,2*2]
print(l)
print(max(lst))
print(min(lst))
print(sum(lst))
l=[1,89,45,12,75,63,12]
ld=sorted(l)
print(ld)
ls=List(hello)
print(ls)


ls=[1,4,5,6,7,8,9]
lst=[2,3]
ls[1]=lst
print(ls)
print(ls[1][1])
lst=[0,1,2,3]
print(all(lst))
print(any(lst)
lst=[1,2,3]
print(1 in  lst)  
print(1 not in lst)


lst=[1,2,3,4,5,6,7,8,9,9]
lst.append(100)
print(lst)
print(lst.count(9))
#count gives no of times number repeated

lst=[1,1,2,2,3,3,4,4,5,5]
print(lst.index(2))

#index function returns its lowest index value


lst=[10,20,30,40,50,60]
lst.insert(1,500)
print(lst)
#insert  list.insert(index,object)
lst.pop()
print(lst)  #pop() deletes last element pop(index)
lst.pop(1)
print(lst)
lst.remove(50)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)

lst=[1,2,3,4,5,6]
lst2=lst
print(lst2) 

#stack using lists
lst=[]
n=int(input("Enter the size of the stack: "))
for i in range(n):
    a=int(input("Enter the {} element: ".format(i)))
    lst.append(a)
l=len(lst)
for i in range(n):
    print(lst[l-1])
    l=l-1
a=int(input("Enter the element to be pushed: "))
lst.append(a)
l=len(lst)
for i in range(n):
    print(lst[l-1])
    l=l-1
lst.pop()
print(lst)


#queues using lists

lst=[]
n=int(input("Enter the size of the queue: "))
for i in range(n):
    x=int(input("Enter {} element: ".format(i)))
    lst.append(x)
l=len(lst)
for i in range(l):
    print(lst[i])
a=int(input("Enter the elmenet to be pushed: "))
lst.insert(l,a)
l=len(lst)
for i in range(l):
    print(lst[i])
print("--------------------------------------------------------------------------")
lst.pop(0)
print("list after pop: ")
l=len(lst)
for i in range(l):
    print(lst[i])


lst=[ i**3 for i in range(10) ]
print(lst)
lst=[1,2,3,4,5,6]
for index,i in enumerate(lst):
    print("{} -> {}".format(index,i))


lst=[ i for i in range(1,21)]
print(lst)
def check(x):
    if(x%2==0 or x%4==0):
        return 1
lt=list(filter(check,lst))
print(lt)

lst=[ i for i in range(1,11)]
print(lst)
def check(x):
    return x**2
lt=list(map(check,lst))
print(lt)

lst=[ i for i in range(1,11)]
def check(x):
    if(x%2!=0):
        return 1
lt=list(filter(check,lst))
print(lt)

lst=[1,2,2,3,4,5,6,7,8,9,9,9,10]
n=int(input("Enter the element to be searched: "))
count=0
for i in range(len(lst)):
    if(lst[i]==n):
        count=count+1
        print("element found at {} index".format(i))
print("NO OF TIMES ELEMENT REPEATED IS ",count)

list=[]
for x in ["hello sai","python"]:
    for y in ["hello","programming"]:
        res=x+y
        list.append(res)
print(list)
list=[1,2,3,4,4,5,3,2,1,7,8,9]
l=len(list)
i=0
while(i<l):
    val=list[i]
    k=len(list)
    for j in range(i+1,k-1):
        im=list[j]
        if(val==im):
            list.pop(j)
    i=i+1
print(list)

lst=["HELLO","PYTHON"]
def convert(x):
    return x.lower()
l=list(map(convert,lst))
print(l)
"""


