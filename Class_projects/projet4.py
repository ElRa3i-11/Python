from random import *
N=int(input("Taper un entier de deux chiffre: "))
M=randint(0,9)
X=(M*100)+N
Y=(N*10)+M
Z=(N//10*100)+(N%10)+(M*10)
print("entier 1:",X)
print("entier 1:",Y)
print("entier 1:",Z)
