def siervo_menu():
    choice = 0

    while choice !=6:
        print("Hello! My name is Jallaine Perpetua G. Siervo.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Durante")
        print("4. Comment from Florido")
        print("5. Comment from Riomalos")
        print("6. Exit")
        choice = input("Enter your choice: ")
        

        match choice:
            
            case '1':
                print("Basic Information:")
                print("Age: 20")
                print("Birthday: August 23, 2004")
                print("Address: Western Bicutan, Taguig City")  
            
            case '2':
                print("Goals:")
                print("Learn more programming languages.")
                print("Graduate college.")
                print("To be successfull in life.")

            case '3':
                print("Florido's Comment: Meow Meow")
    
            case '6':
                print("Exiting the program.")
                exit()

siervo_menu()