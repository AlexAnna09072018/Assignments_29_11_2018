def mbt(b):
    i=0
    c=[]
    for i in range(0,len(b)):
        c.append(b[i]*2)
        i=i+1
        if i==len(b):
            return c
