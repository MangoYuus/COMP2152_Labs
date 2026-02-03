# Question 5: Contact Book (Dictionaries - Basic Operations)
contacts = {
    "Joy": "555-1234",
    "Roy": "555=4321",
    "Zoy": "555-1324"
}
print(f"Roy's number: {contacts["Roy"]}")
contacts["Simon"] = "555-9999"
print(f"Coontacts after Adding Simon: {contacts}")
contacts["Roy"] = "666-1234"
print(f"Coontacts after Updating Roy: {contacts}")
del contacts["Zoy"]
print(f"Coontacts after Deleting Zoy: {contacts}")

print(f"All Names: {contacts.keys()}")
print(f"All Numbers: {contacts.values()}")
print(f"Total Users: {len(contacts)}")