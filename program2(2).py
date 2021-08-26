def sumsquare(l):
    out = []
    e, o = 0, 0
    for i in range(0, len(l)):
        if l[i]%2 == 0:
            e = e + l[i]**2
        else:
            o = o + l[i]**2
    out.append(o)
    out.append(e)
    return out
