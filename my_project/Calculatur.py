from math import*
test = True
while test :
    Choice = input("how many numbers you will calculate \n1,2,3,4 : ")
    if Choice == "1":
        Premier = float(input("input number: "))
        if Choice == "1":
            ParameterComplexe = input("Complexe operation:\nabsolute,square root :")
            if ParameterComplexe not in ("1", "2", "3", "4"):
                print("operation invalid")
            else:
                print("operation valid")
                if ParameterComplexe == "1":
                    print("you chosed to absolute the number")
                    print("|", Premier, "|", "=", abs(Premier))
                if ParameterComplexe == "2":
                    print("you chosed to square root the number")
                    print(sqrt(Premier))
            wh = input("do you want to continue\n(y to continue , n to decline): ")
            if wh == "y":
                test = True
            else:
                test = False
    elif Choice == "2":
        Premier = float(input("input the first number: "))
        Seconder = float(input("input the second number: "))
        Parameter_decider = input("chosse simple or complex operation: ")
        if Parameter_decider not in ("1","2") :
            print("operation invalid try again")
        else:
            if Parameter_decider == "2":
                ParameterComplexe = input("Complexe operation:\nabsolute,Power,Integer division,Modulo: ")
                if ParameterComplexe not in ("1", "2", "3", "4","5"):
                    print("operation invalid")
                else:
                    print("operation valid")
                    if ParameterComplexe == "1":
                        Abs = input("what number you will absolute")
                        if Abs == "1":
                            print("you chosed to absolute the first number")
                            print("|", Premier, "|", "=", abs(Premier))
                        else:
                            print("you chosed to absolute the second number")
                            print("|", Seconder, "|", "=", abs(Seconder))
                    if ParameterComplexe == "2":
                        print("you chosed Power fonction: ")
                        print(Premier, "**", Seconder, "=", Premier ** Seconder)
                    if ParameterComplexe == "3":
                        print("you chosed Integer fonction: ")
                        print(Premier, "//", Seconder, "=", Premier // Seconder)
                    if ParameterComplexe == "4":
                        print("you chosed Modulo fonction: ")
                        print(Premier, "%", Seconder, "=", Premier % Seconder)
                    if ParameterComplexe == "5":
                        print("you chosed to square root the number")
                        print(sqrt(Premier))
            elif Parameter_decider == "1" :
                Parameter = input("enter the fonctions below\nsimple operation:\n+,-,*,/: ")
                if Parameter not in ("+", "-", "*", "/"):
                    print("operation invalid")
                else:
                    print("operation valid")
                    if Parameter == "/":
                        divsion = input("What number will you divsion?\n the first number(1) , or the second(2)")
                        if divsion == 1:
                            print("you chosse :", Premier, "/", Seconder)
                            print(Premier, "/", Seconder, "=", Premier / Seconder)
                        else:
                            print("you chosse :", Seconder, "/", Premier)
                            print(Seconder, "/", Premier, "=", Seconder / Premier)
                    if Parameter == "-":
                        sub = input('What number will you subtract? \n the first number(1) , or the second(2)')
                        if sub == '1':
                            print("you chosse :", Premier, "-", Seconder)
                            print(Premier, "-", Seconder, "=", Premier - Seconder)
                        else:
                            print("you chosse :", Seconder, "-", Premier)
                            print(Seconder, "-", Premier, "=", Seconder - Premier)

                    else:
                        if Parameter == "+":
                            print("you chose: ", Parameter)
                            print(Premier, Parameter, Seconder, "=", Premier + Seconder)
                        elif Parameter == "*":
                            print("you chose: ", Parameter)
                            print(Premier, Parameter, Seconder, "=", Premier * Seconder)
        wh=input("do you want to continue\n(y to continue , n to decline): ")
        if wh == "y" :
            test = True
        else:
            test = False
    elif Choice == "3":
        Premier = float(input("input the first number: "))
        Seconder = float(input("input the second number: "))
        Third = float(input("input the third number: "))
        Parameter_decider = input("chosse simple or complex operation: ")
        if Parameter_decider not in ("1", "2"):
            print("operation invalid try again")
        else:
            if Parameter_decider == "2":
                ParameterComplexe = input("Complexe operation:\nabsolute,Power,Integer division,Modulo,squart root: ")
                if ParameterComplexe not in ("1", "2", "3", "4", "5"):
                    print("operation invalid")
                else:
                    print("operation valid")
                    if ParameterComplexe == "1":
                        Abs = input("what number you will absolute")
                        if Abs == "1":
                            print("you chosed to absolute the first number")
                            print("|", Premier, "|", "=", abs(Premier))
                        elif Abs =="2":
                            print("you chosed to absolute the second number")
                            print("|", Seconder, "|", "=", abs(Seconder))
                        else:
                            print("you chosed to absolute the second number")
                            print("|", Third, "|", "=", abs(Third))
                    if ParameterComplexe == "2":
                        print("you chosed Power fonction: ")
                        print(Premier, "**", Seconder,"**",Third, "=", Premier ** Seconder**Third)
                    if ParameterComplexe == "3":
                        print("you chosed Integer fonction: ")
                        print(Premier, "//", Seconder,"//",Third ,"=", Premier//Seconder//Third)
                    if ParameterComplexe == "4":
                        print("you chosed Modulo fonction: ")
                        print(Premier, "%", Seconder,"%",Third, "=", Premier%Seconder%Third)
                    Sqrt1 = input("what number you will Squart root")
                    if Sqrt1 == "1":
                        print("you chosed to sqrt the first number")
                        print(sqrt(Premier))
                    elif Sqrt1 == "2":
                        print("you chosed to sqrt the second number")
                        print(sqrt(Seconder))
                    else:
                        print("you chosed to sqrt the second number")
                        print(sqrt(Third))
            elif Parameter_decider == "1":
                Parameter = input("enter the fonctions below\nsimple operation:\n+,-,*,/: ")
                if Parameter not in ("+", "-", "*", "/"):
                    print("operation invalid")
                else:
                    print("operation valid")
                    if Parameter == "/":
                        divsion3 = str(input("Write the eqaution\n(rewrite the number like this ff/ss/tt): ")) # 45/63/5
                        indiceDivsion=[]
                        i = divsion3.find("/")
                        while i!=-1 :
                            indiceDivsion.append(i)
                            i=divsion3.find("/",i+1)
                        firstnum=int(divsion3[:indiceDivsion[0]])
                        secondnum=int(divsion3[indiceDivsion[0]+1:indiceDivsion[1]])
                        thirdnum=int(divsion3[indiceDivsion[1]+1:])
                        print("your typed",divsion3)
                        print("result: ",firstnum/secondnum/thirdnum)
        wh = input("do you want to continue\n(y to continue , n to decline): ")
        if wh == "y":
            test = True
        else:
            test = False

