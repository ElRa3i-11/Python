from math import*
from random import randint

N=input("saisir un mot")
print("le long de mot",len(N))
X=float(input("saisir un nombre avec des décimales"))
print(abs(X))
print("l'arondi a l'entier plus proche",round(X))
print("le partie entier",trunc(X))
print("la racince caréé du nombre",sqrt(X))
Y=randint(1,50)
print(X>Y or X<Y)
U=ord(N[0])
print(U)
print(chr(U))

