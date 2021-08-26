
#1
def expanding(l):
  x=[]
  y=0
  for i in range (len(l)-1):
    y= l[i]-l[i-1]
    if y<0:
      y=-1*y
    x.append(y)
  for j in range(len(x)-1):
    if abs(x[j])<abs(x[j-1]):
      return False
    j+=1
  return True
