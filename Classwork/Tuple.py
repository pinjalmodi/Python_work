t=(1,2,1.1,2,2,10,20,[100,200,300],"tops",True,"python",1,2)

print(t)
print(t.count(1))
print(t.index(10))
print(t[6])
t[6].append(400)
print(t)
for i in t:
    print(i)
print(1.2 in t)
