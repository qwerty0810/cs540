import sys
import math
import string

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        X = dict.fromkeys(string.ascii_uppercase, 0)
        for line in f:
            uppercase = line.upper().strip()
            for i in uppercase:
                if i.isalpha():
                    X[i] += 1

    return X

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

X=shred("letter.txt")
print("Q1")
for key, value in X.items():
    print(key, value)
e,s=get_parameter_vectors()

print("Q2")
x1=X["A"]
print(round(x1*math.log(e[0]), 4))
print(round(x1*math.log(s[0]), 4))

def crack(eng, spa, dict):
    i=0
    Feng = 0.0
    Fspa = 0.0
    for key in dict.keys():        
        Feng += (math.log(eng[i])*dict[key])
        Fspa += (math.log(spa[i])*dict[key])
        i += 1   
    Feng += math.log(0.6)
    Fspa += math.log(0.4)
    p = -1
    print("Q3")
    print("{:.4f}".format(Feng,4))
    print("{:.4f}".format(Fspa,4))
    
    if((Fspa - Feng) >= 100):
        p = 0
    elif((Fspa - Feng) <= -100):
        p = 1
    else: 
        p = 1/(1 + (math.e**(Fspa - Feng)))
    print("Q4")
    print("{:.4f}".format(p,4))
    
def main():
    crack(e, s, X)
main()


