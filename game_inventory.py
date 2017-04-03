# inventory-system for games

backpack = {"torch":2, "coins":42, "dagger":1}

def displayInventory(inventory):
	print("Inventory:")
	total_items = 0
	for k, v in inventory.items():
		print(str(v) + " " + k)
		total_items += v
	print(str(total_items) + " Total Items")

displayInventory(backpack)
