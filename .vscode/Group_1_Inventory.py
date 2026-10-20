# Requirement 1: Define pre-approved hardware models.
# Tuples are immutable (read-only)
approved_models = ("MacBook Pro", "Dell XPS", "ThinkPad")

# Requirement 2: Identify new list for storage.
# Mutable list to update inventory []
device_inventory = []


def display_menu():
    print("\n- Group 1: Inventory Management -")
    print("Select from options 1-4 to proceed. ")


# Requirement 3: Persistent interactive menu loop.
# The infinite loop keeps the program running until break
while True:
    display_menu()
    choice=input(" 1: Add\n 2: Remove\n 3: Verify\n 4: Exit\n")
    # Requirement 4: Option 1. Validate input before appending.
    if choice == "1":
        model = input("Enter device model: ")
        if model in approved_models:
            device_inventory.append(model)
            print(model + " added to inventory.")
        else:
            print("Error: Device model not approved for company use.")

    # Requirement 5: Option 2. Verify the item exists before removing it.
    elif choice == "2":
        # Prompt user for item to remove
        device = input("Enter device to remove: ")
        # Safe existence check before removal (prevents ValueError)
        if device in device_inventory:
            device_inventory.remove(device)
            print("Device removed.")
        else:
            # Graceful error handling
            print("Device not found.")

    # Requirement 4: Option 3. Display current device inventory.
    elif choice == "3":
        # Print active inventory list
        print("Current Active Stock:", device_inventory)

        # Show how many of each approved model are in stock
        print("\nQuantity by Model:")
        for model in approved_models:
            print(model, str(device_inventory.count(model)))
        print("Total devices: ", str(len(device_inventory)))

    # Option 4: Explicit exit signal ends the loop.
    elif choice == "4":
        print("Exiting Inventory Management. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")