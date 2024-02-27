items = ['apple', 'banana', 'orages', "apple", "dragonfruit"]
# items.insert(2, "TEST")
# print(items)
items[3:3] = ["TE", "ST"]
print(items)
items.sort(key=str.lower)
print(items)

items_copy = items[:]
print(items_copy)
