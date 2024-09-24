L = []
for i in range(1,11):
    fac = 1
    for j in range(1,i+1):
        fac *= j
    L.append(fac)
    
print(L)