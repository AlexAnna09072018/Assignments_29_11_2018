#variant 1  

def phonebook(name,location):
    i=0
    c=0
    dict={}
    for i in range(0,len(name)):
        dict[name[i]]=location[c]
        c+=1
        i+=1
        if i==len(name):
            print dict 
