l=[1,2,3,4,5]
max=l[0]
sec_max=l[0]
for i in l:
    if i>max:
        sec_max=max
        max=i
    elif i>sec_max and i!=max:
        sec_max=i
        
print(max)
print(sec_max)
