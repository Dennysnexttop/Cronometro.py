import time

choix = input("enter 1 to get a chronometer "
              "\nenter 2 pto get a timer "
              "\n-> ")
chronometre = False
decompte = False

if(choix == "1") :
    minutes = 0
    secondes = 1

    minutes = int(minutes)
    secondes = int(secondes)
    IsOver = False

    while (IsOver == False):
        print("")
        print("")
        print(str(minutes) + " minutes " +
            "\net " + str(secondes) + " secondes")
        secondes = secondes + 1
        if (secondes >= 60):
            minutes = minutes + 1
            secondes = 0
        elif (minutes >= 60) :
            IsOver = True
        else :
            nothing = True
        time.sleep(1)


elif(choix == "2") :
    minutes = 0
    secondes = 0
    minutes = input("enter the minutes"
                    "\n(max : 60)-> ")
    secondes = input("enter the seconds"
                     "\n(max : 60)-> ")
    minutes = int(minutes)
    secondes = int(secondes)
    IsOver = False

    while (IsOver == False):
        print("")
        print("")
        print(str(minutes) + " minutes " +
            "\net " + str(secondes) + " secondes")
        secondes = secondes - 1
        if (secondes <= -1):
            minutes = minutes - 1
            secondes = 59
        elif(secondes <= 0 and minutes <= 0) :
            IsOver = True
            time.sleep(1)
            print("")
            print("")
            print("0 minutes \nand 0 seconds")
            print("")
            print("timer over !")
        else :
            nothing = True
        time.sleep(1)

else :
    print("relance the script \nand enter 1 or 2")
