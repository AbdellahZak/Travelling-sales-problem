# Name: Abdellah Zakani
# Student ID: 009970024

import csv
from Package import Package
from HashTable import HashTable
import Truck
import datetime

with open("Data/packages.csv", 'r', encoding="utf-8-sig") as csv_file:
    myHash = HashTable()
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:  # Time complexity of O(N)
        p = Package(pid=line[0], address=line[1], city=line[2], state=line[3],
                    zipcode=line[4], deadline=line[5], weight=line[6], notes=line[7], status="At Hub")
        myHash.insert(int(p.pid), p)

# for i in range(len(myHash.table)):
#    print("Package: {}".format(myHash.search(i + 1)))
# Read the file of distances information
with open("Data/Distance_File.csv") as csvfile: # Time complexity O(1)
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file of address information
with open("Data/Address_File.csv") as csvfile1: # Time complexity O(1)
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)


# finding distance between two addresses
def distance_between_adds(x, y): # Time complexity O(1)
    distance = CSV_Distance[x][y]
    if distance == '':
        distance = CSV_Distance[y][x]

    return float(distance)


# get the index of the location string
def extract_address(address): # Time complexity O(1)
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Create truck object truck1
truck1 = Truck.Truck(16, 18, [1, 4, 7, 8, 13, 14, 15, 16, 29, 30, 31, 32, 34, 37, 40, 39], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck.Truck(16, 18, [3, 18, 36, 38, 6, 10, 11, 12, 17, 20, 21, 22, 23, 24, 25, 26], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck.Truck(16, 18, [9, 19, 27, 28, 33, 35, 2, 5], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))


def deliver_packages(truck_object):
    # putting truck packages in the to deliver list
    to_deliver = []
    for packageId in truck_object.packages: # Time complexity O(n)
        package = myHash.search(packageId)
        to_deliver.append(package)
    # will need to clear the package ids in the truck package list, to be put back(delivered) later.
    truck_object.packages.clear()
    # adding packages to truck object, nearest neighbor first
    while len(to_deliver) > 0: # Time complexity O(n2)
        next_address = 500
        next_package = None
        for package in to_deliver:
            # Compare addresses and finding the shortest distance
            if distance_between_adds(extract_address(truck_object.address),
                                     extract_address(package.address)) <= next_address:
                next_address = distance_between_adds(extract_address(truck_object.address),
                                                     extract_address(package.address))
                next_package = package
        # Add package to the truck package list ie "Delivered"
        truck_object.packages.append(next_package.pid)
        # Removes the same package from the to deliver list
        to_deliver.remove(next_package)
        # Add driven mileage to truck mileage attribute
        truck_object.mileage += next_address
        # Updates truck's current address
        truck_object.address = next_package.address
        # Updates the time it took for the truck to drive to the nearest package
        truck_object.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck_object.time
        next_package.depart_time = truck_object.depart_time


deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)


class Main: # Time complexity O(1)
    # this is command interface the user will be using to request data from the program.
    print("The mileage for this specific route is:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)  # total mileage for all trucks
    try:
        # The user will be asked to enter a specific time
        user_time = input("Please enter a time during the travel of the route. Use the format, Hour:Minutes  ")
        (h, m) = user_time.split(":")
        current_time = datetime.timedelta(hours=int(h), minutes=int(m))
        # user will have to choose the type of output requested individual package or all packages
        input_2 = input("To view the status of an individual package please type '1'. For all:  "
                        " packages please type 'all'.  ")
        if input_2 == "1":
            try:
                # if single package was chosen, output individual package.
                packageId = input("Enter the package ID  ")
                package = myHash.search(int(packageId))
                package.update_status(current_time)
                print(str(package))
            except ValueError:
                print("Entry not recognised. will close program.")
                exit()
        elif input_2 == "all":
            try:
                for packageID in range(1, 41): # Time complexity O(n) n=40
                    package = myHash.search(packageID)
                    package.update_status(current_time)
                    print(str(package))
            except ValueError:
                print("Entry not recognised. will close program.")
                exit()
        else:
            exit()
    except ValueError:
        print("Entry not recognised. will close program.")
        exit()
