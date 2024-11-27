
choice = 0
while choice !=4:
    print("Herchel Modules")
    print("1. Riomalos Module")
    print("2. Zyrrah Module")
    print("3. Run all")
    print("4. Steph Module")
    print("5. exit")
    print(" ")
    choice = input("Enter your choice: ")

    match choice:

        case '1':
            from herchel_package import rio_module

            rio_module.numpy_operations()
        
        case '2':
            from herchel_package import zy_module

            zy_module.show_month_calendar()
            
            zy_module.is_leap_year()
        
        case '3':
            from herchel_package import zy_module, rio_module
            
            print("Numpy Operations")
            rio_module.numpy_operations()

            print("\nCalendar")
            zy_module.show_month_calendar()
            zy_module.is_leap_year()

        case '4':
            from herchel_package import steph_module
            steph_module.tell_joke()
        
        case '5':
            exit()