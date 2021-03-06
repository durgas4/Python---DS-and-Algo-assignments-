#1
#Write a Python function histogram(l) that takes as input a list of integers
#with repetitions and returns a list of pairs as follows:.

#(1)for each number n that appears in l,
#there should be exactly one pair (n,r) in the list returned by the function, where r is the number of repetitions of n in l.

#(2)the final list should be sorted in ascending order by r,
#the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

#For instance:

#>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
#[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

#2
#A college maintains academic information about students in three separate lists

#Course details: A list of pairs of form (coursecode,coursename), where both entries are strings. For instance,
#[ ("MA101","Calculus"),("PH101","Mechanics"),("HU101","English") ]

#Student details: A list of pairs of form (rollnumber,name), where both entries are strings. For instance,
#[ ("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar") ]

#A list of triples of the form (rollnumber,coursecode,grade), where all entries are strings. For instance,
#[ ("UGM2018001", "MA101", "AB"), ("UGP2018132", "PH101", "B"), ("UGM2018001", "PH101", "B") ].
#You may assume that each roll number and course code in the grade list appears in the student details and course details, respectively.

#Your task is to write a function transcript (coursedetails,studentdetails,grades)
#that takes these three lists as input and produces consolidated grades for each student.
#Each of the input lists may have its entries listed in arbitrary order. Each entry in the returned list should be a tuple of the form

#(rollnumber, name,[(coursecode_1,coursename_1,grade_1),...,(coursecode_k,coursename_k,grade_k)])

#where the student has grades for k >= 1 courses reported in the input list grades.

#The output list should be organized as follows.

#The tuples shold sorted in ascending order by rollnumber

#Each student's grades should sorted in ascending order by coursecode

#For instance
#>>>transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2021001","Rohit Grewal"),
#("UGP2021132","Neha Talwar")],[("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")])

#[('UGM2021001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]),
#('UGP2021132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]



def build_table(l):
    # Use a dictionary to build a frequency table
    frequency = {}

    # For each number, create a new entry in the table or increment the frequency
    for n in l:
        if n in frequency.keys():
            frequency[n] = frequency[n] + 1
        else:
            frequency[n] = 1

    return(frequency)

def sort_table(fdict):
    # First build a list of the form (r,n)
    flist = [ (fdict[n],n) for n in fdict.keys() ]

    # Sort this list using built in sort, which will sort first by frequency, then by value
    flist.sort()

    # Flip each pair and return
    return( [ (n,r) for (r,n) in flist ])

def histogram(l):
    frequency_table = build_table(l)
    return(sort_table(frequency_table))

def transcript(coursedetails,studentdetails,grades):

    coursedict = setup_coursedict(coursedetails)
    studentdict = setup_studentdict(studentdetails)
    gradedict = setup_gradedict(grades)


    outputlist = []

    for r in sorted(gradedict.keys()):
        gradelist = []
        for (ccode,grade) in sorted(gradedict[r]):
            gradelist.append((ccode,coursedict[ccode],grade))

        outputlist.append((r,studentdict[r],gradelist))

    return(outputlist)

def setup_coursedict(details):

    dict = {}
    for (ccode,cname) in details:
        dict[ccode] = cname

    return(dict)

def setup_studentdict(details):

    dict = {}
    for (rollno,name) in details:
        dict[rollno] = name

    return(dict)

def setup_gradedict(details):

    dict = {}
    for (rollno,ccode,grade) in details:
        if rollno in dict.keys():
            dict[rollno].append((ccode,grade))
        else:
            dict[rollno] = [(ccode,grade)]

    return(dict)


# Hidden code below

import ast

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "histogram":
   arg = ast.literal_eval(farg)
   print(histogram(arg),end="\n")
elif fname == "transcript":
   arg = ast.literal_eval(farg)
   print(transcript(arg[0],arg[1],arg[2]),end="\n")
else:
   print("Function", fname, "unknown")
