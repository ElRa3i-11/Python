N=input("entrer your name")
print("the lenght of your name",len(N))
print("your name is",N.upper())
print("Is decimal:", N.isdecimal())
if N.isdecimal():
    print("As int:", int(N))
    print("As float:", float(N))
else:
    print("Not convertible to number")