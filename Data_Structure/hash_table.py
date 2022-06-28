stock_prices = []
with open('data.csv', 'r') as f:
    for line in f:
        day, price = line.split(',')
        price = float(price)
        stock_prices.append([day, price])

# print(stock_prices)

# Find stock price
for element in stock_prices:
    if element[0] == '6-Mar':
        print(element[1])

# Process using python dictionary
stock_prices = {}
with open('data.csv', 'r') as f:
    for line in f:
        day, price = line.split(',')
        price = float(price)
        stock_prices[day] = price

print(stock_prices)


# ********************************************************* Implement Hash Table ***************************************************
def get_hash(key):
    sum = 0
    for c in key:
        sum += ord(c)
    return sum % 100

print(get_hash('6-Mar'))

# ****************************************************** Implement Hash Table *********************************************************
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None]*self.MAX

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

h = HashTable()
h['6-Mar'] = 5          # set item
del h['6-Mar']          # del item
print(h['6-Mar'])       # get item