#disctionaries

dog = {"name" : "heli", "age" :8, "color" : "blonde"}
print(dog["name"])
dog["name"] = "anti"
print(dog)
#if you allready have a value of color you cant change it with .get
print(dog.get("color", "brown"))