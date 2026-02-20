from random import*
x=int(input("tpaer l'entier du participan 1: "))
y=int(input("tpaer l'entier du participan 2: "))
if x>y :
    Mi=y
    Ma=x
elif y>x :
    Mi=x
    Ma=y
E=randint(Mi,Ma)
print("l'entier choisi par l'ordinateur est",E)
if E%2 == 0 :
    print("le premier participant gagné")
else :
    print("le deuxiéme participant a gagné")
