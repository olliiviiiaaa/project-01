# Define the list of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print the list of authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to display the main menu and handle user input
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. Exit")
        
        # Get user input
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

# Start the program
menu()
