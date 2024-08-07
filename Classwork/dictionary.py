d={145:"Ajay",908:"Vijay",765:"Jay",654:"Kamal",999:"Karan"}

print(d)
print(d[908])
print(d.get(765))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(908))
print(d)
print(d.popitem())
print(d)
d1={1:"Vijay",2:"Karan",145:"Ketan"}
d.update(d1)
print(d)
for i in d:
    print(i,":",d[i])
