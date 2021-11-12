"""dict={}
print(dict)
d={1:"sai"}
print(d)
d={1:"sai",2:"teja"}
print(d[1])
print(d[2])
print(d)
d[3]="sunny"
print(d)
d[3]="leone"
print(d)

d={1:"sai",2:"teja",3:"lion"}
print(d)
del d[2]
print(d)
d.clear()
print(d)
d={"name":"saiteja","course":"btech"}
print(d)
d.pop("name")
print(d)
d.pop()
print(d)"""
l=["name","age"]
s=["sai teja",18]
d=dict(zip(l,s))
print(d)