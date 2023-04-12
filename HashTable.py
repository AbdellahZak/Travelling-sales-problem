# this was adapted from Cemal Tepe video on hashtable


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