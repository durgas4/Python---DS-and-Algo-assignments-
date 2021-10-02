#1
#Write a function expanding(l)
#that takes as input a list of integer l and returns True
#if the absolute difference between each adjacent pair of elements strictly increases.
# >>> expanding([1,3,7,2,9])
  #True
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
      
#2
#Write a Python function sumsquare(l) that takes a nonempty list of
#integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers
#in l and even is the sum of squares of all the even numbers in l
#>>> sumsquare([1,3,5])
#[35, 0]
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
  
#3
#A two dimensional
#matrix can be represented in Python row-wise, as a list of lists:
#each inner list represents one row of the matrix. For instance, the matrix
#1  2  3  4
#5  6  7  8
#would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].
def transpose(m):
    l = []
    a = []
    for j in range(len(m[0])):
        for i in range(len(m)):
            l.append(m[i][j])
        a.append(l)
        l=[]

    return a 
