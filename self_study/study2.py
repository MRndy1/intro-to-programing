# print("This is upper".isupper())
# book1 = True
# book2 = False
#
# read_book = any([book1, book2])
# print(read_book)
#
# num1 = complex(2,3)
# print(num1.real, num1.imag)

#a list can hold different data type
dogs = ['cat', 'dog', 'dat', True, 1]
print(1 in dogs)
dogs[2] = "doggies"
print(dogs[2])
print(dogs[-1])
print(dogs[2:])
print(len(dogs))

dogs.append("heli")
print(dogs)
dogs.extend(["anti", "mimi", "momo"])
dogs += [90, 93]
print(dogs)
dogs.remove("mimi")
print(dogs)