N=int(input("Taper un entier former de trois chiffre: "))
C=N//100
U=N%10
D=N%100//10
S=C+D+U
A=C*D*U
print("la masse de",N,"est",S)
print("l'accroissement de",N,"est",A)
