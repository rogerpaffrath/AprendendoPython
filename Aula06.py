# LISTS -> DYNAMIC SIZE, CAN HAVE REPEATED ITEMS
# CREATING EMPTY LIST
alerts =[]

# CREATING LIST WITH VALUES
alerts = ["sub gift","hype train","bits"]

# ADDING ITEMS TO THE END OF A LIST
alerts.append("sub")
alerts.append("follow")
print(alerts)

# ADDING BEFORE THE INDEX PROVIDED
alerts.insert(1, "raid")
print(alerts)

# REMOVING THE LAST ITEM
alerts.pop()
print(alerts)

# REMOVING THE FIRST OCCURANCE OF A VALUE
alerts.remove("hype train")
print(alerts)

# COUNT THE NUMBER OF OCCURENCES
print(alerts.count("raid"))

# TUPLE -> SIMILAR TO THE LIST, BUT IMMUTABLE
favorite_viewers = tuple(("guilherme_zm", "andreacarmoo", "pdrucorreia", "yoyoturbo"))
print(favorite_viewers)

# ACCESSING VALUES
print(favorite_viewers[0])

# SEARCHING VALUES
print("Index of 'andreacarmoo':", favorite_viewers.index("andreacarmoo"))

# SET -> HAS NO DUPLICATE ITEMS, UNORDERED
dogs = set() 

dogs.add("Rockynho") # First, there was Rockynho
dogs.add("Rogerinho") # Then, we adopted Rogerinho
dogs.add("Rogerinho") # No error, but it is impossible to add another Rogerinho

print(dogs)

# DICTIONARY -> INDEXED WITH KEY->VALUE
client = {
    "name"    : "John Doe",
    "age"     : 54,
    "address" : "258, 32st New York, NY"
    }
print(client)
print(client["name"])

# GET ALL VALUES
print(client.values())

# GET ALL KEYS
print(client.keys())

# REMOVING THE GIVEN KEY (RETURNS VALUE)
print(client.pop("address"))
print(client)

# REMOVE ALL KEYS AND VALUES
client.clear()
print(client)