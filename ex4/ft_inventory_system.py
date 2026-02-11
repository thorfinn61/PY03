import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    # Flake8 préfère un alignement suspendu ou visuel précis
    numbers = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    inventory = {}
    total_items = 0
    for arg in sys.argv[1:]:
        name = ""
        quantity = ""
        reading_name = True

        for char in arg:
            if char == ':':
                reading_name = False
            elif reading_name:
                name = name + char
            else:
                quantity = quantity + char

        # Conversion
        current_item_qty = 0
        for number in quantity:
            current_item_qty = current_item_qty * 10 + numbers[number]

        # Mise a jour inventory
        value = inventory.get(name)
        if value:
            inventory.update({name: value + current_item_qty})
        else:
            inventory.update({name: current_item_qty})

        # Mise a jour total
        total_items = total_items + current_item_qty

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        qty = quantity
        percentage = (qty / total_items) * 100
        print(f"{item}: {qty} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    max_qty = 0
    max_name = ""
    min_qty = total_items
    min_name = ""
    for name, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_name = name
        if qty < min_qty:
            min_qty = qty
            min_name = name

    print(f"Most abundant: {max_name} ({max_qty} units)")
    print(f"Least abundant: {min_name} ({min_qty} units)")

    print("\n=== Item Categories ===")
    moderate_inv = {}
    scarce_inv = {}
    for item, quantity in inventory.items():
        if quantity > 3:
            moderate_inv.update({item: quantity})
        else:
            scarce_inv.update({item: quantity})

    print(f"Moderate: {moderate_inv}")
    print(f"Scarce: {scarce_inv}")

    print("\n=== Managment Suggestions ===")
    restock = []
    for item, quantity in inventory.items():
        if quantity == 1:
            restock = restock + [item]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    dic_keys = []
    dic_values = []
    for item, quantity in inventory.items():
        dic_keys = dic_keys + [item]
        dic_values = dic_values + [quantity]
    print(f"Dictionary keys: {dic_keys}")
    print(f"Dictionary values: {dic_values}")

    is_found = False
    if "sword" in inventory:
        is_found = True
    print(f"Sample lookup - 'sword' in inventory: {is_found}")
