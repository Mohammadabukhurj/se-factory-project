def running_program():
    running= True
    while running == True:
        print("Hello! Please enter: ")
        print("1. To go to the drivers' menu")
        print("2. To go to the cities' menu")
        print("3. To exit the system")
        user_input = int(input())
        if user_input == 1:
            drivers_menu()
        elif user_input == 2:
            cities_menu()
        elif user_input == 3:
            print("Exiting System...")
            running = False


def drivers_menu():
    while True:
        if user_input_drivers == 1:
            print("Hello to the drivers menu! Please enter:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To go back to main menu")
            user_input_drivers = int(input())
            for i in drivers_list:
                print(i+", "+drivers_list[i][0]+", "+drivers_list[i][1])
        elif user_input_drivers == 2:
            add_driver()
        elif user_input_drivers == 3:
            return



def add_driver():
    pass




def cities_menu():
    pass







drivers_list = {"ID001":["Max Verstappen","Akkar"],"ID002":["Charles Leclerc","Saida"],"ID003":[" Lando Norris","Jbiel"]}
running_program()