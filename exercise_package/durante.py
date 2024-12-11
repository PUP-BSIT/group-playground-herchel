def durante_menu():
    choice = 0
    
    while choice !=6:
        print("Hi! I'm Stephanie V. Durante")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment from Florido")
        print("4. Comment from Riomalos")
        print("5. Comment from Siervo")
        print("6. exit")

        choice = input("Enter your choice:")

        match choice:

            case '1':
                print("Basic Information:")
                print("Age: 19 years old")
                print("Birthday: February 22, 2005")
                print("Hobby: reading books, listening to music")

            case '2':
                print("Goals:")
                print("To graduate")
                print("Gain certifications")
                print("Build a personal project portfolio")

            case '3':
                print("Florido's Comment: Meow Meow")

            case '5':
                print("Hello this is my comment.")

            case '4':
                print("Riomalos comment: Hwaiting!")

            case '6':
                exit()