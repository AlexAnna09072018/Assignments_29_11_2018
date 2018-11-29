#the comment for the tasks Ah yes and some comments. I was avoiding the solutions you offered, such as zip and one line list-item multiplications, I know that they exist 


def mbt(b):
    i=0
    c=[]
    for i in range(0,len(b)):
        c.append(b[i]*2)
        i=i+1
        if i==len(b):
            return c
