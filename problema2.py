import copy
a=[[1,2,3],[4,5,6]]
b=a
print("a and b before modify")
print(a)
print(b)
a[0][1]=10
print("a and b after modify")
print(a)
print(b)

b=copy.deepcopy(a)
print("a and b before modify")
print(a)
print(b)
a[0][1]=9
print("after")
print(a)
print(b)