#3
def transpose(m):
    l = []
    a = []
    for j in range(len(m[0])):
        for i in range(len(m)):
            l.append(m[i][j])
        a.append(l)
        l=[]

    return a 
  
