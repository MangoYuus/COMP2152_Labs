# Question 2 : Shopping Cart (Lists = Searching and Removal)
cart = ["apple", "banana", "bread", "milk", "eggs", "apple", "mango"]
apple_count = cart.count("apple")
print("We have", apple_count, "apples")
print("Position of Milk:", cart.index("milk"))
#remove
cart.remove("apple")
print("Removed item using pop:", cart.pop())
#确认某个item是否在cart里
print("Is banana in the cart? ", "banana" in cart)
print("The Final Cart: ",cart)