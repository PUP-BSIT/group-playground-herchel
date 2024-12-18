UNSET_OPTION = 0
EXIT_OPTION = 5
choice = UNSET_OPTION

while choice != EXIT_OPTION:
    print("\n=== Main Menu ===")
    print("1. Durante")
    print("2. Florido")
    print("3. Riomalos")
    print("4. Siervo")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1: 
            # TODO(Durante): call the menu in your module
            pass
        case 2:
            from herchelpackage import florido
            
            christmas = florido.Christmas.display_menu()
        case 3:
            # TODO(Riomalos): call the menu in your module
            pass
        case 4:
            from herchel.siervo import GradeManagementSystem
            
            grades = GradeManagementSystem()
            grades.display_menu()
            pass
        case 5:
            pass
        case _:
            print("\nError: Invalid input. "
                  + "Please enter a number between 1 and 5.")
