#1
def factor(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst=lst+[i]
    return(lst)
def isprime(o):
    return(factor(o)==[1,o])          

def primeproduct(m):
    lists=[]
    for p in range (2,m+1):
        for q in range (2,p):
            if isprime(q):
                if isprime(p):
                    if m==p*q:
                      return True
                   
    else:
        return False
