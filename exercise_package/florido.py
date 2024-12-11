def florido_menu():
    choice = 0

    while choice != 6:
        print("Good day! I am Maydelyn B. Florido.")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment from Durante")
        print("4. Comment from Riomalos")
        print("5. Comment from Siervo")
        print("6. Exit")

    match choice:
        case '1':
            print("Basic Information:")
            print("Sex: Female")
            print("Age: 19 years old")
            print("Birtdate: June 07 2005")

        case '2': 
            print("Goals:")
            print("1. Graduate college")
            print("2. Get a job")
            print("3. Be rich")

        case '4':
            print('Riomalos comment: Hwaiting!')
            
        case '6':
            exit()