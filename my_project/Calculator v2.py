equation=input("note:you can only choose 6 number: ")
test=True
i=0
indice=[]
a=equation.find("/")
b=equation.find("+")
c=equation.find("-")
d=equation.find("*")
for i in range(len(equation)) :
    while True :
        if a != -1:
            a = equation.find("/", a + 1)
            indice.append(a)
        elif b != -1:
            b = equation.find("+", b + 1)
            indice.append(b)
        elif c != -1:
            c = equation.find("-", c + 1)
            indice.append(c)
        elif d != -1:
            d = equation.find("*", d + 1)
            indice.append(d)
        break
first=int(equation[:indice[0]])
second=int(equation[indice[0]+1:indice[1]])
third=int(equation[indice[1]+1:indice[2]])
forth=int(equation[indice[2]+1:indice[3]])
fifth=int(equation[indice[3]+1:indice[4]])
sixth=int(equation[indice[4]+1:indice[5]])
print(equation,"=",first+second+third+forth+fifth+sixth)

