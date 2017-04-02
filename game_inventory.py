# inventory-system for games

backpack = {"torch":2, "coins":42, "dagger":1}

def displayInventory(inventory):
	print("Inventory:")
	total_items = 0
	for k, v in inventory.items():
		print(k + str(v))
		total_items += v
	print("Total Items: " + str(total_items))

displayInventory(backpack)
