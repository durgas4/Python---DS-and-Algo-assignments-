def primeproduct(m):
    x=[]
    for i in range(2,m+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            x.append(i)
    for i in range(0,len(x)):
        for j in range(0,len(x)):  #2*2=4 and both the multiple are prime factor
            if(x[i]*x[j]==m):
                return True #here what i tried doing is check if m is a product of the prime numbers so true if found else false
    else:
        return False
