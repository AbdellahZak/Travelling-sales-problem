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
    def __init__(self, intruck):
        self.myTruck = intruck


class Truck:
    def __init__(self, packages):
        self.packages = packages


class Package:
    def __init__(self, pid, address, deadline, city,state ,zipcode, weight, status, notes):
        self.pid = pid
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state=state
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

with open("distances.csv", 'r', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    x=csv_reader.keys()
    print (x)
    for line in csv_reader:
        print(line)
