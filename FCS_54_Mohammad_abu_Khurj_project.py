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
        elif user_input == 3:
            print("Exiting System...")
            running = False


def drivers_menu():
    print("Hello to the drivers menu! Please enter:")
    print("1. To view all the drivers")
    print("2. To add a driver")
    print("3. To go back to main menu")
    user_input_drivers = int(input())
    if user_input_drivers == 1:
        view_drivers()
    elif user_input_drivers == 2:
        add_driver()
    elif user_input_drivers == 3:
        return

def view_drivers():
    for i in drivers_list:
        print(i+", "+drivers_list[i][0]+", "+drivers_list[i][1])

def add_driver():
    pass




def cities_menu():
    pass







drivers_list = {"ID001":["Max Verstappen","Akkar"],"ID002":["Charles Leclerc","Saida"],"ID003":[" Lando Norris","Jbiel"]}
running_program()