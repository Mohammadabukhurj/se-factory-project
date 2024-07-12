def running_program():
    running= True
    while running == True:
        print("Hello! Please enter: ")
        print("1. To go to the drivers' menu")
        print("2. To go to the cities' menu")
        print("3. To exit the system")
        print("\t")
        user_input = int(input("Your choice:"))
        print("\t")
        if user_input == 1:
            drivers_menu()
        elif user_input == 2:
            cities_menu()
        elif user_input == 3:
            print("Exiting System...")
            running = False


def drivers_menu():
    while True:
        print("\t")
        print("Hello to the drivers menu! Please enter:")
        print("1. To view all the drivers")
        print("2. To add a driver")
        print("3. To go back to main menu")
        print("\t")
        user_input_drivers = int(input("Your choice for the drivers menu:"))
        print("\t")
        if user_input_drivers == 1:
            print("---------------------")
            for i in drivers_list:
                print(i+", "+drivers_list[i][0]+", "+drivers_list[i][1])
            print("\t")
            print("---------------------")    
        elif user_input_drivers == 2:
            new_driver()
            print(drivers_list)
        elif user_input_drivers == 3:
            return
        else:
            print("This input is invalid")



def new_driver():
  input_driver_name = input("What is the name of the driver?:")
  input_driver_city = input("What is the start city of the driver?:")
  dictionary_size = str(len(drivers_list)+1)
  driver_ID = "ID00"+dictionary_size
  drivers_list[driver_ID]=[input_driver_name,input_driver_city]





def cities_menu():
    pass







drivers_list = {"ID001":["Max Verstappen","Akkar"],"ID002":["Charles Leclerc","Saida"],"ID003":[" Lando Norris","Jbiel"]}
running_program()