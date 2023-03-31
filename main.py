import csv


class HashTable:
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, key, item):
        slot = hash(key) % len(self.table)
        slot_list = self.table[slot]

        # update if exists
        for keyValue in slot_list:
            if keyValue[0] == key:
                keyValue[1] == item
                return True
        # if not
        key_value = [key, item]
        slot_list.append(key_value)
        return True

    def search(self, key):
        slot = hash(key) % len(self.table)
        slot_list = self.table[slot]

        for keyValue in slot_list:
            if keyValue[0] == key:
                return keyValue[1]  # value
        return None


class Driver:
    def __init__(self):
        self


driver1 = Driver
driver2 = Driver


class Truck:
    def __init__(self, packages, driver):
        self.packages = packages
        self.driver = driver


truck1 = Truck
truck2 = Truck
Truck3 = Truck


class Package:
    def __init__(self, pid, address, deadline, city, state, zipcode, weight, status, notes):
        self.pid = pid
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.status = status
        self.notes = notes

    def __str__(self):  # overwrites print(package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s , %s, %s " % (
            self.pid, self.address, self.deadline, self.city, self.zipcode, self.weight, self.status, self.notes)


with open("packages.csv", 'r', encoding="utf-8-sig") as csv_file:
    myHash = HashTable()
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        p = Package(pid=line[0], address=line[1], city=line[2], state=line[3],
                    zipcode=line[4], deadline=line[5], weight=line[6], notes=line[7], status="default")
        myHash.insert(int(p.pid), p)

'''for i in range(len(myHash.table)):
    print("Package: {}".format(myHash.search(i + 1)))'''
with open("addresses.csv", 'r', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    addresses = []
    for line in csv_reader:
        addresses.append(line[0])


def measure_distance(x, y):
    index = addresses.index(x)
    with open("distances2.csv", 'r', encoding="utf-8-sig") as csv_file_dict:
        csv_reader_dict = csv.DictReader(csv_file_dict)
        line_number = 0
        distance = 0
        for row in csv_reader_dict:
            if line_number == index:
                distance = row[y]
                return distance
            else:
                line_number += 1


'''def min_distance(x):
    distance_list = []
    for i in addresses:
        z = measure_distance(i, x)
        if z == "":
            z = measure_distance(x, i)
        else:
            distance_list.append(z)
            distance_list.sort()
    return distance_list[1]'''


print(min_distance('600 E 900 South'))
