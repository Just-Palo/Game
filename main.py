print("***Welcome to the zombie infestation clear up unit***")


def menu():
    while True:

        play = "Play"
        turnoff = "Quit"
        print("**Play**")
        print("**Quit**")
        choose = input("Choose option: ")

        if choose == play:
            print("**Starting game**")
            print("Loading:25%")
            print("Loading:50%")
            print("Loading:90%")
            print("Loading:100%")

        elif choose == turnoff:
            print("**Quiting game**")
            break