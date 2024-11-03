
# Fractional Knapsack Problem

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractionalknapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    totalprice = 0
    remainingcapacity = capacity

    for item in items:
        if item.weight <= remainingcapacity:
            totalprice += item.value
            remainingcapacity -= item.weight
        else:
            fraction = remainingcapacity / item.weight
            totalprice += item.value * fraction
            break

    return totalprice

items = [Item(10, 2), Item(20, 3), Item(30, 4), Item(40, 5)]
capacity = 10

totalprice = fractionalknapsack(items, capacity)
print("Total price:", totalprice)