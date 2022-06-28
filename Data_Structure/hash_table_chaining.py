# Hash Table Collision Handling Using Chaining
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):

            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] =(key, val)
                found = True
        
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print(f"deleting element at index {index}")
                del self.arr[arr_index][index]

h = HashTable()
h['6-Mar'] = 5              # set item
h['6-Mar'] = 52             # set item
h['8-Mar'] = 3              # set item
h['9-Mar'] = 45             # set item
h['17-Mar'] = 2             # set item
h['20-Mar'] = 59            # set item
del h['6-Mar']              # del item
print(h.arr)                # get item