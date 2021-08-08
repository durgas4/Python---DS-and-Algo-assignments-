def delchar(s,c):
    x=""
    if len(c)==1:
        for i in s:
            if i!=c :
                x=x+i
        return (x)
    else:
        return (s)
