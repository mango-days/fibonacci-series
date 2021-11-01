k=12
a=0
b=1
array=[]
for i in range (0, k):
    array.append(a)
    temp = a+b
    b=a
    a=temp
print(array)