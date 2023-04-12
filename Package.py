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
        self.depart_time = 0
        self.delivery_time = 0

    def __str__(self):  # overwrites print(package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s , %s, %s " % (
            self.pid, self.address, self.deadline, self.city, self.zipcode, self.weight, self.status, self.notes)

    def update_status(self, timedelta):
        if self.delivery_time < timedelta:
            self.status = "Delivered"
        elif self.depart_time > timedelta:
            self.status = "En route"
        else:
            self.status = "At Hub"
