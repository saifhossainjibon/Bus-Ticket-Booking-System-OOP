class Bus:
    def __init__(self,number,route,total_seats):
        self.number=number
        self.route=route
        self.total_seats=total_seats
        self.booked_seats=0

    def available_seats(self):
        unbooked_seats = self.total_seats- self.booked_seats
        return unbooked_seats
    
    def book_seat(self):
        if self.available_seats() > 0 :
            self.booked_seats+=1
            return True
        return False
    

class Passenger:
    def __init__(self,name,phone,bus):
        self.name=name
        self.phone=phone
        self.bus=bus

class BusSystem:
    def __init__(self):
        self.bus_list=[]
        self.passenger_list=[]

    def add_bus(self, number, route, seats):
        new_bus = Bus(number,route,seats)
        self.bus_list.append(new_bus)
    
    def book_ticket(self,bus_number, name, phone):
        if self.bus_list:
            for bus in self.bus_list:
                if bus_number == bus.number:
                    if bus.book_seat():
                        passenger = Passenger(name, phone, bus)
                        self.passenger_list.append(passenger)
                        print("Ticket Booked !!!")
                    else:
                        print("No seat Available")
                    return
        else:
            print("No Bus Available")       

    def show_buses(self):
        if self.bus_list:
            print("--- Available Buses ---")
            for bus in self.bus_list:
                print(f"Bus Number: {bus.number} Available Seats: {bus.available_seats()}")
        else:
            print("No Bus Available")

class Admin:
    def __init__(self):
        self.username="admin"
        self.password="1234"

    def login(self,username,password):
        return self.username == username and self.password == password
    


admin=Admin()
system=BusSystem()

while True:
    print("/---- Main Menu -----/")
    print("- 1. Admin Login")
    print("- 2. Book Ticket")
    print("- 3. View Buses")
    print("- 4. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        username= input("Enter Your Username: ")
        password= input("Enter Your Password: ")
        if admin.login(username,password):
            while True:
                print("/---- Admin Menu -----/")
                print("-- 1. Add Bus")
                print("-- 2. View All Buses")
                print("-- 3. Logout")
                admin_choice= int(input(" Enter your Choice: "))
                if admin_choice == 1:
                        number = input("Bus Number: ")
                        route = input("Route: ")
                        seats = int(input("Total Seats: "))
                        system.add_bus(number, route, seats)
                elif admin_choice == 2:
                    system.show_buses()
                elif admin_choice == 3:
                    break
                else:
                    print("Wrong Input, please try again")

        else:
            print("Wrong Username or Password")

    elif choice == 2:
        bus_number=input("Enter the Bus Number: ")
        name=input("Enter the Passenger Name: ")
        phone=input("Enter the Passenger phone number: ")
        system.book_ticket(bus_number,name,phone)
        print("Ticket Fare 500 tk")

    
    elif choice == 3:
        system.show_buses()
    
    elif choice == 4:
        break
    else: 
        print("Wrong Input, please try again")

    

    



