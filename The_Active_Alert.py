# Empty List to track alerts
alert_queue = []

threat_levels = ("Critical", "Suspicious")

while True:
    print("\n SOC Active Alert Queue ")
    print("\n1. Log New Alert\n2. View Active Queue\n3. Resolve Oldest Alert\n4. Exit System")

    choice = input("Select an option (1-4): ")
# New Entry - Add user input to alert_queue
    if choice == "1":
        threat = input("Name New Alert: ")
        threat_level = input("Enter Threat Level (1-2): ")
        if threat_level == "1":
            alert_queue.append(("Critical Alert: ",threat))
        elif threat_level == "2":
            alert_queue.insert(0,("Suspicious Alert: ", threat))
        else:
                print("Invalid Option, Select digit 1 or 2")
        print("Alert logged successfully!")
# Pending Alerts
    elif choice == "2":
        print(" - Pending Alerts - ")
        # If the list is empty, this loop simply doesn't run
        # Print a numbered list of items in alert_queue(Starting at 1)
        for number, alert in enumerate(alert_queue, start=1):
            print(f"{number}. {alert}")
# Resolve Oldest Alert
# Remove item at index 0 and assign to a variable 
# pop.()

#Must check list length before attempting to pop an item - Will cause IndexError is list is empty
    elif choice == "3":
        if len(alert_queue) > 0:
            resolved_threat = alert_queue.pop(0)
            print(f"Resolved and cleared: {resolved_threat}")
        else:
            print("No pending alerts. The queue is clear.")
# Exit option - break while loop
    elif choice == "4":
        print("Exiting system. Goodbye, Analyst.")
        break
# Prevent crash if user input isnt 1-4
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")