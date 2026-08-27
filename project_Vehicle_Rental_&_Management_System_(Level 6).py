#🚗 Project: Vehicle Rental & Management System (Level 6)
import ast

vehicle_data = {}


def add_vehicle_through(vehicle_data):
    through_count = 0
    for key, value in vehicle_data.items():
        through_count += 1

    while True:
        through_count += 1

        owner_name = input("Enter Name :")

        try:
            age = int(input("Enter Age :"))
        except ValueError:
            age = int(input("Enter Age :"))

        try:
            vehicle_no = int(input("Enter Vehicle Number :"))
        except ValueError:
            vehicle_no = int(input("Enter Vehicle Number :"))


        vehicle_type = input("Enter vehicle Type :")
        vehicle_name = input("Enter vehicle Name :")
        brand = input("Enter vehicle Brand :")

        try:
            model = int(input("Enter vehicle Model :"))
        except ValueError:

            model = int(input("Enter vehicle Model :"))

        color = input("Enter vehicle Color  :")
        try:
            rental_price = int(input("Enter rental Price :"))
        except ValueError:
            print("you enter wrong data type. please enter a number here 👇")
            rental_price = int(input("Enter rental Price :"))

        vehicle_data["vehicle" + str(through_count)] = {
            "owner_name": owner_name,
            "age": age,
            "vehicle_Detials": {
                "vehicle_no": vehicle_no,
                "vehicle_type": vehicle_type,
                "vehicle_name": vehicle_name,
                "brand": brand,
                "model": model,
            },
            "color": color,
            "rental_price": rental_price,
        }

        exit_add = input("Do you want to exit the \"press\" enter :")
        if exit_add == "":
            break


def display_vehicles(vehicle_data1):
    dis_count = 0
    for key, value in vehicle_data1.items():
        dis_count += 1

    def great(n):

        if n == 0:
            return 0
        great(n - 1)
        print(vehicle_data1["vehicle" + str(n)])

    great(dis_count)


def search_vehicles(vehicle_data2):

    search_vehicle = int(input("Search vehicle by number :"))
    for key, value in vehicle_data2.items():
        if search_vehicle == value["vehicle_Detials"]["vehicle_no"]:
            print(key, value)
            break
    else:
        print("Vehicle is not found")


def rent_vehicles(vehicle_data):
    total_price = 0
    vehicle_number_rent = 0
    Customer_name = input("Enter Customer Name :")
    vehicle_number = int(input("Enter Vehicle Number :"))
    day = int(input("how many day you want to rent :"))

    x = 0

    for key, value in (vehicle_data.items()):

        x += 1

        if vehicle_number == value["vehicle_Detials"]["vehicle_no"]:
            try:
                del vehicle_data[key]["rented vehicle"]
            except:
                print("there is no vehicle is returned")
            vehicle_number_rent += value["rental_price"]
            total_price += vehicle_number_rent * day
            vehicle_data["vehicle" + str(x)]["rented vehicle"] = {
                "Customer_name": Customer_name,
                "vehicle_number": vehicle_number,
                "day": day,
                "total_rent_price": total_price,
            }
            print(f"You will pay for {day} days :{total_price} pesos")
            break
    else:
        print("No vehicle found")

    return vehicle_number


def return_vehicles_(vehicle_data,):
    return_rent_vehicles = int(input("Enter the number of Vehicle :"))
    for key, value in vehicle_data.items():
            try:
                if return_rent_vehicles == value["vehicle_Detials"]["vehicle_no"]:
                    if return_rent_vehicles == value["rented vehicle"]["vehicle_number"]:
                        del vehicle_data[key]["rented vehicle"]
                        print(f"vehicle number {return_rent_vehicles} is returned")
                        #vehicle_data[key]["return vehicle"] = return_rent_vehicles
                        break
            except KeyError:
                print("You must to take first a vehicle on rent")

    else:
        print("please check you number")


def calculate_Tax(rented_vehicle_number ,vehicle_data ):
    Tax_rat = 10
    rent_price = 0
    for key, value in vehicle_data.items():
        if rented_vehicle_number == value["vehicle_Detials"]["vehicle_no"]:
            if rented_vehicle_number == value["rented vehicle"]["vehicle_number"]:
                rent_price = value["rented vehicle"]["total_rent_price"]
                Tax = (Tax_rat / 100) * rent_price
                vehicle_data[key]["rented vehicle"]["Tax"] = Tax
                print("tax is added to the main dictionary")
                break
    else:
        print("please check you number or there is no rented vehicles")


def statistics(vehicle_data,rented_vehicle_number):

    Iterate = 0
    total_tax = 0

    highest_rental_price = -0
    lowest_rental_price = float("inf")

    total_rental_price = 0

    for key, value in vehicle_data.items():
        Iterate += 1
        if highest_rental_price < value["rental_price"]:
            highest_rental_price = value["rental_price"]
        if lowest_rental_price > value["rental_price"]:
            lowest_rental_price = value["rental_price"]

        if "rented vehicle" in value:
            if "Tax" in value["rented vehicle"]:
                total_tax += value["rented vehicle"]["Tax"]

        if value["rental_price"] == value["rental_price"]:
            total_rental_price += value["rental_price"]

    average_rental_price = total_rental_price / Iterate

    print(f"The highest rental price is :{highest_rental_price}")
    print(f"The lowest rental price is: {lowest_rental_price}")
    print(f"The average rental price is: {average_rental_price}")
    print(f"Total vehicles is: {Iterate}")
    print(f"Total tax are : {total_tax}")


def count_vowels():
    vowels = ["a","e","i","o","u" ,"A","E","I","O","U"]
    count_vowels = 0
    for key, value in vehicle_data.items():
        for y in value["owner_name"]:
            if y in vowels:
                count_vowels += 1

    print(f"Total vowels : {count_vowels}")


def sort_price_name_lambada(vehicle_data):
    x = sorted(vehicle_data.items() ,key=lambda y: y[1]["rental_price"])
    print(x)
    x1 = sorted(vehicle_data.items(), key=lambda y1: y1[1]["rental_price"] ,reverse=True)
    print(x1)
    x2 = sorted(vehicle_data.items(), key=lambda y2: y2[1]["owner_name"])
    print(x2)


def store_data_through_file(vehicle_data):
    with open("vehicle_data.txt", "w") as f:
        f.write(str(vehicle_data))


def load_data(vehicle_data):
    try:
        with open("vehicle_data.txt", "r") as f:
            data = f.read()

            vehicle_data.update(ast.literal_eval(data))

            print("Data loaded successfully")

    except FileNotFoundError:
        print("No saved file found!")
    except (ValueError ,SyntaxError):
        print("The ile fil contains invalid data!")

load_data(vehicle_data)


def summery(vehicle_data):
    highest_rental_price = -0
    lowest_rental_price = float("inf")

    total_vehicles = 0
    available_vehicles = 0
    rented_vehicles = 0
    average_rental_price = 0
    total_tax = 0

    for key, value in vehicle_data.items():
        total_vehicles += 1
        if "rented vehicle" in value:
            rented_vehicles += 1
        else:
            available_vehicles += 1


        #find highest price and lowest
        if highest_rental_price < value["rental_price"]:
            highest_rental_price = value["rental_price"]
        if lowest_rental_price > value["rental_price"]:
            lowest_rental_price = value["rental_price"]

        #find Average price
        if "rental_price" in value:
            average_rental_price += value["rental_price"]

        if "rented vehicle" in value:
            if "Tax" in value["rented vehicle"]:
                total_tax += value["rented vehicle"]["Tax"]


    average = average_rental_price / total_vehicles

    print(f"Total vehicles are :{total_vehicles}")
    print(f"available vehicles are :{available_vehicles}")
    print(f"rented vehicles are :{rented_vehicles}")
    print(f"The highest rental price is :{highest_rental_price}")
    print(f"The lowest rental price is: {lowest_rental_price}")
    print(f"The average rental price is: {average}")
    print(f"Total tax is :{total_tax}")


def menu():
    while True:
        enter_data = input("if you want to enter data then write \"YES\" or if not the write \"NO\" :")
        if enter_data == "YES" or enter_data == "yes":
            add_vehicle_through(vehicle_data)

        display_data = input("if you want to display data then write \"YES\" or if not the write \"NO\" :")
        if display_data == "YES" or display_data == "yes":
            display_vehicles(vehicle_data)

        search = input("if you want to search data then write \"YES\" or if not the write \"NO\" :")
        if search == "YES" or search == "yes":
            search_vehicles(vehicle_data)

        rent = input("if you want to take a vehicle on rent then write \"YES\" or if not the write \"NO\" :")
        rented_vehicle_number = None
        if rent == "YES" or rent == "yes":
            rented_vehicle_number = rent_vehicles(vehicle_data)
            calculate_Tax(rented_vehicle_number, vehicle_data)

        #rented_vehicle_number = rent_vehicles(vehicle_data, rented_vehicle)

        return_ = input("if you want to return vehicle then write \"YES\" or if not the write \"NO\" :")
        if return_ == "YES" or return_ == "yes":
            return_vehicles_(vehicle_data)

        #tax = input("if you want to calculate tax then write \"YES\" or if not then write \"NO\" :")
        #if tax == "YES":
            #calculate_Tax(rented_vehicle_number, vehicle_data)

        statis = input("if you want to show statistics then write \"YES\" or if not the write \"NO\" :")
        if statis == "YES" or statis == "yes":
            statistics(vehicle_data, rented_vehicle_number)

        vowels = input("if you want to show vowels then write \"YES\" or if not the write \"NO\" :")
        if vowels == "YES" or vowels == "yes":
            count_vowels()

        sort = input("if you want to sort data through lowest to highest and highest to lowest and also by owner name."
                     "write \"YES\" or if not the write \"NO\" :")
        if sort == "YES" or sort == "yes":
            sort_price_name_lambada(vehicle_data)

        store_data = input("if you want to store data into data.py file then write \"YES\" or if not the write \"NO\" :")
        if store_data == "YES" or store_data == "yes":
            store_data_through_file(vehicle_data)

        sumr = input("if you want to show summary. the write \"YES\" or not the write \"NO\" :")
        if sumr == "YES" or sumr == "yes":
            summery(vehicle_data)

        exit = input("If you want to exit. then press \"enter\" :")
        if exit == "":
            break

menu()

