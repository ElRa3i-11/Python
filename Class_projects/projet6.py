nom=input("taper votre prenom")
Date=input("taper votre date de naisscense")
P=nom[0]
F=nom[len(nom)-1]
J=int(Date[:2])
M=int(Date[3:5])
A=int(Date[6:len(Date)])
Poid=A+J+M
print(Poid)
print(P)
print(F)


