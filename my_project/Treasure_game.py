Test = True
while Test :
    lucky_word = input("enter the lucky word: ")
    Winning_door = (len(lucky_word) * 3) % 10
    Guess = 0
    Attmepts = 4
    Doors = ["Door1", "Door2", "Door3", "Door4", "Door5", "Door6", "Door7", "Door8", "Door9", "Door10"]
    First_Door = 0
    Second_Door = 0
    Third_Door = 0
    print(Doors)
    Test = True
    Test2 = True
    for i in range(3):
        Attmepts = Attmepts - 1
        print("Attempts left= ", Attmepts)
        if Attmepts == 4:
            print(Doors)
        if First_Door in Doors:
            if Attmepts == 3:
                Doors.remove(First_Door)
                print(Doors)
        if Second_Door in Doors:
            if Attmepts == 2:
                Doors.remove(Second_Door)
                print(Doors)
        if Third_Door in Doors:
            if Attmepts == 1:
                Doors.remove(Third_Door)
                print(Doors)
        Guess = int(input("Which the the door that have Treasure: "))
        if Guess > 0:
            if Attmepts == 4:
                First_Door = "Door" + str(Guess)
            elif Attmepts == 3:
                Second_Door = "Door" + str(Guess)
            elif Attmepts == 2:
                Third_Door = "Door" + str(Guess)
        if Guess == Winning_door:
            print("You Won :)")
            Test2 = True
            while Test2:
                t = input("Do you want to Continue another game Y(yes),Or,N(no): ")
                tm = t.upper()
                if tm == "YES" or tm == "Y":
                    Test = True
                    Test2 = False
                elif tm == "NO" or tm == "N":
                    Test = False
                    Test2 = False
                else :
                    Test2 = True
        if Winning_door > Guess:
                print("The treasure is behind a higher-numbered door")
        if Winning_door < Guess:
                print("The treasure is behind a lower-numbered door")
        if Attmepts == 1 and Guess != Winning_door:
                print("You lost :(")
                Test2=True
                while Test2:
                    t = input("Do you want to Continue another game Y(yes),Or,N(no): ")
                    tm = t.upper()
                    if tm == "YES" or tm == "Y":
                        Test = True
                        Test2 = False
                    elif tm == "NO" or tm == "N":
                        Test = False
                        Test2 = False
                    else :
                        Test2 = True

