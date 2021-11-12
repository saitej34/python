"""lis=[1,2,3,4,5,6,1,2,3]
tup=(1,2,3,4,5,6,7,1,2,3,4,5)
print(set(lis))
print(set(tup))

#addition using lists
lis1=[]
lis2=[]
m=int(input("Enter the no of rows: "))
n=int(input("Enter the no of columns: "))
k=0
    for i in range(m):
    lis2=[]
    for j in range(n):
        a=int(input("Enter the list[{}][{}] element: ".format(i,j)))
        lis2.append(a)
    lis1.append(lis2)
    k=k+1
print(lis1)

for i in range(m):
    for j in range(n):
        print(lis1[j][i],end=" ") #transpose
    print()
lis4=[]
for i in range(m):
    lis3=[]
    for j in range(n):
        a=int(input("Enter the list[{}][{}] element: ".format(i,j)))
        lis3.append(a)
    lis4.append(lis3)
print(lis4)

for i in range(m):
    for j in range(n):
        print(lis1[i][j]+lis4[i][j],end=" ")
    print()"""