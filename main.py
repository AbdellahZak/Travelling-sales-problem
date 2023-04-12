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
    for line in csv_reader:
        p = Package(pid=line[0], address=line[1], city=line[2], state=line[3],
                    zipcode=line[4], deadline=line[5], weight=line[6], notes=line[7], status="At Hub")
        myHash.insert(int(p.pid), p)

# for i in range(len(myHash.table)):
#    print("Package: {}".format(myHash.search(i + 1)))

with open("Data/Distance_File.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file of address information
with open("Data/Address_File.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)


# finding distance between two addresses
def distance_between_adds(x, y):
    distance = CSV_Distance[x][y]
    if distance == '':
        distance = CSV_Distance[y][x]

    return float(distance)


# address number from string of address
def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Create truck object truck1
truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))


def deliver_packages(truck_object):
    # putting truck packages in the to deliver list
    to_deliver = []
    for packageId in truck_object.packages:
        package = myHash.search(packageId)
        to_deliver.append(package)
    # will need to clear the package ids in the truck package list, to be put back(delivered) later.
    truck_object.packages.clear()
    # adding packages to truck object, nearest neighbor first
    while len(to_deliver) > 0:
        next_address = 500
        next_package = None
        for package in to_deliver:
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
        next_package.departure_time = truck_object.depart_time


deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)


class Main:
    # Interface
    print("The mileage for the route is:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)  # total mileage for all trucks
    try:
        # The user will be asked to enter a specific time
        user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM  ")
        (h, m) = user_time.split(":")
        timedelta = datetime.timedelta(hours=int(h), minutes=int(m))
        input_2 = input("To view the status of an individual package please type '1'. For all"
                        " packages please type 'all'.")
        if input_2 == "1":
            try:
                solo_input = input("Enter the numeric package ID  ")
                package = myHash.search(int(solo_input))
                package.update_status(timedelta)
                print(str(package))
            except ValueError:
                print("Entry invalid. Closing program.")
                exit()
        elif input_2 == "all":
            try:
                for packageID in range(1, 41):
                    package = myHash.search(packageID)
                    package.update_status(timedelta)
                    print(str(package))
            except ValueError:
                print("Entry invalid. Closing program.")
                exit()
        else:
            exit()
    except ValueError:
        print("Entry invalid. Closing program.")
        exit()
