import csv
from Package import Package
from HashTable import HashTable
from Truck import Truck
import datetime

with open("Data/packages.csv", 'r', encoding="utf-8-sig") as csv_file:
    myHash = HashTable()
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        p = Package(pid=line[0], address=line[1], city=line[2], state=line[3],
                    zipcode=line[4], deadline=line[5], weight=line[6], notes=line[7], status="default")
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


class Main:
    print("This is the user interface")
