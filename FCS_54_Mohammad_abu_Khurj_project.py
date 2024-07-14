class Graph:
    def __init__(self,Nodes):
      self.nodes = Nodes
      self.adj_list = {}    

      for node in self.nodes:
          self.adj_list[node] = []

    def print_list(self):
      for node in self.nodes:
          print(node, "-(neighburing)->", self.adj_list[node])

    def add_edge(self,a,b):
        self.adj_list[a].append(b)
        self.adj_list[b].append(a)


def running_program():
    running= True
    while running == True:
        print("\t")
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
            if len(drivers_list) == 20:
                print("Can't add anymore!")
            else:
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
    if (len(Cities_list) <= 15):
        for i in range(len(Cities_list)):
            if input_driver_city.lower() != Cities_list[i].lower():
                print("This city doesn't exit in our list, adding this city to the list")
                Cities_list.append(input_driver_city)
                break
            else:
                print("City already in list")
                break

        print(Cities_list)

        if len(dictionary_size) == 2:
            driver_ID = "ID0"+dictionary_size
        elif len(dictionary_size) == 1:
            driver_ID = "ID00"+dictionary_size
        else:
            driver_ID = "ID"+dictionary_size
        drivers_list[driver_ID]=[input_driver_name,input_driver_city]
    else:
        print("List is full!")




def cities_menu():
    while True:
        print("\t")
        print("Hello! Welcome to cities menu! Please enter:")
        print("1. Show cities")
        print("2. Print neighbouring cities")
        print("3. Print drivers delivering to city")
        print("4. Return to main program")
        print("\t")
        user_input_cities = int(input("Your choice for cities menu:"))
        print("\t")
        if user_input_cities == 1:
            print(Cities_list)
        elif user_input_cities == 2:
            print_neighbur_cities()
        elif user_input_cities == 3:
            print_drivers_delivering_to_city()
        elif user_input_cities == 4:
            return




def print_neighbur_cities():
    nodes = ["Saida","Zahle","Beirut","Jbeil","Akkar"]
    edges = [("Saida","Zahle"),("Beirut","Jbeil"),("Akkar","Jbeil")]

    graph_cities = Graph(nodes)
    for a,b in edges:
        graph_cities.add_edge(a,b)
    graph_cities.print_list()
    return

def print_drivers_delivering_to_city():
    pass

Cities_list = ["Saida","Zahle","Beirut","Jbeil","Akkar"]

drivers_list = {"ID001":["Max Verstappen","Akkar"],"ID002":["Charles Leclerc","Saida"],"ID003":[" Lando Norris","Jbiel"]}
running_program()