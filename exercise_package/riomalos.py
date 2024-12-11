def riomalos_menu():
    choice = 0
    while choice !=6:
        print("\nHello I am Zyrrah Feil C. Riomalos")
        print("1. Basic Information")
        print("2. My Goals")
        print("3. Comment from Florido")
        print("4. Comment from Siervo")
        print("5. Comment from Durante")
        print("6. Exit")
        print(" ")
        choice = input("Enter your choice: ")

        match choice:

            case '1':
                print("\n\tBasic Information")
                print('Name                : Zyrrah Feil C. Riomalos')
                print('Age                 : 19')
                print('Birthday            : September 24, 2005')
                print('Chinese Zodiac Sign : Rooster')
                print('Zodiac Sign         : Libra')
                print('Hobby               : Watching K-Drama, Play online games')
                print(input())
                
            case '2':
                print('\n\tMy Goals')
                print('- To graduate college.')
                print('- Earn more skills on programming.')
                print('- Avoid procrastination.')
                print('- Develop time management and self-discipline.')
                print(input())

            case '6':
                exit()

if __name__ == "__main__":
    riomalos_menu()