while True:
    try:
        Temp = int(input("enter your number: "))

        if Temp <90 and Temp >60:
                print ("warm")
        elif Temp >=90:
                print ("hot")
        else:
                print ("chilly")
    except ValueError:
        print ("no dumb ass")
        continue
