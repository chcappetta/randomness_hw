import numpy
import random


p = 10/random.randint(1,1000)
q = 10/random.randint(1,1000)
num = 1000000
k = 3

sumx = 0
givcount = 0
mincount = 0
totalmax = 0
equal = 0
i = 0

while i < num:
    x = 1
    while random.random() > p:
        x += 1
    y = 1
    while random.random() > q:
        y += 1
    if x == y:
        equal += 1
    if min(x,y) == k:
        mincount+=1
    if x<= y:
        sumx += x
        givcount +=1
    if x > y:
        totalmax += x
    else: totalmax += y
    i += 1



probability = equal/num
thinkprob = (p*q)/(p+q-p*q)
Emax = totalmax/num
thinkEmax = (1/p)+(1/q)-(1/(p+q-p*q))
minim = mincount/num
thinkminim = ((1-p)**(k-1))*((1-q)**(k-1))*(p+q-p*q)
giv = sumx/givcount
thinkgiv = 1/(p+q-p*q)
print("Think P(X = Y) = ", thinkprob)
print("P(X = Y) = ", probability)
print("Think E[max(X,Y)] = ", thinkEmax)
print("E[max(X,Y)] = ", Emax)
print("Think P(min(X,Y)) = ", thinkminim)
print(" P(min(X,Y)) = ", minim)
print("Think E[X|X<=Y]) = ", thinkgiv)
print("E[X|X<=Y]) = ", giv)




