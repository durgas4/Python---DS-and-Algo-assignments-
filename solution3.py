#1
#Write a function expanding(l)
#that takes as input a list of integer l and returns True
#if the absolute difference between each adjacent pair of elements strictly increases.
# >>> expanding([1,3,7,2,9])
  #True

      
#2
#Write a Python function sumsquare(l) that takes a nonempty list of
#integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers
#in l and even is the sum of squares of all the even numbers in l
#>>> sumsquare([1,3,5])
#[35, 0]

#3
#A two dimensional
#matrix can be represented in Python row-wise, as a list of lists:
#each inner list represents one row of the matrix. For instance, the matrix
#1  2  3  4
#5  6  7  8
#would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

def expanding(l):
    if len(l) <= 2:
        return(True)
    diff = abs(l[1]-l[0])
    return(diff < abs(l[2]-l[1]) and expanding(l[1:]))

def expanding_iterative(l):
    if len(l) <= 2:
        return(True)
    olddiff = abs(l[1]-l[0])
    for i in range(2,len(l)):
        newdiff = abs(l[i]-l[i-1])
        if newdiff <= olddiff:
            return(False)
        olddiff = newdiff
    return(True)

####################

def even(n):
    return(n%2 == 0)

def sumsquare(l):
    oddsum = 0
    evensum = 0
    for n in l:
        if even(n):
            evensum += n*n
        else:
            oddsum += n*n
    return([oddsum,evensum])

###################

def transpose(l):
  outl = []
  for row in l[:1]:
    for i in range(len(row)):
      outl.append([])
  for row in l:   
    for i in range(len(row)):
      outl[i].append(row[i])
  return(outl)

###################

import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "expanding":
  arg = parse(farg)
  print(expanding(arg))

if fname == "sumsquare":
  arg = parse(farg)
  print(sumsquare(arg))

if fname == "transpose":
  arg = parse(farg)
  savearg = arg
  ans = transpose(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")

