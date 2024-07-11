def running_program():
    print("Hello! Please enter: ")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")
    running= True
    user_input = int(input())
    while running == True:
        if user_input == 1:
            drivers_menu()
        elif user_input == 2:
            cities_menu()
        else:
            print("Exiting System...")
            running = False


def drivers_menu():
    pass


def cities_menu():
    pass


running_program()