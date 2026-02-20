from numpy import array
test=True

n1_test2=True
n1_test3=True
n1_test4=True
n1_test5=True
n1_diviseur_2=array([int]*10)
n1_diviseur_3=array([int]*10)
n1_diviseur_4=array([int]*10)
n1_diviseur_5=array([int]*10)
n1_x1=0
while test:
    choose=input("will calculate pgcd or ppcm")
    if choose == "1":
        print("You will calculate the pgcd")
        n1=int(input("choose the first number: "))
        n2=int(input("choose the second number: "))
        if n1 % 2 == 0:
            while n1_test2:
                if n1%2 == 0:
                    print(n1)
                    n1=n1//2
                    print(n1)
                    n1_diviseur_2=[+str(2)+]
                else :
                    print(n1_diviseur_2)
                    n1_test2=False
            if n1 % 3 == 0:
                while n1_test3:
                    if n1%3 == 0:
                        if n1%3 == 0:
                            print(n1)
                            n1=n1//3
                            print(n1)
                            n1_diviseur_3 = [str(3)]
                        else :
                            n1_test3=False
                            print(n1_diviseur_3)
                if n1%4==0 :
                    while n1_test4:
                        if n1 % 4 == 0:
                            if n1 % 4 == 0:
                                print(n1)
                                n1 = n1 // 4
                                print(n1)
                                n1_diviseur_4 = [str(4)]
                            else:
                                n1_test4 = False
                                print(n1_diviseur_4)
                    if n1%5==0 :
                        while n1_test3:
                            if n1 % 5 == 0:
                                if n1 % 5 == 0:
                                    print(n1)
                                    n1 = n1 // 5
                                    print(n1)
                                    n1_diviseur_5 = [str(5)]
                                else:
                                    n1_test3 = False
                        if n1%n1 == 0 :
                            print(n1)
                            n1_x1=n1
                            n1=n1//n1
        if n1==0:
            test=False
print(n1_x1)