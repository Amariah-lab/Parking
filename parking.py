import time
num_slots = 5
cost_per_hour = 10
parking_slots = [None] * num_slots
def find_empty_slot():
    for i in range(num_slots):
        if parking_slots[i] == None:
            return i
    return None
def park_vehicle():
    empty_slot = find_empty_slot()
    if empty_slot == None:
        print("Sorry, the parking lot is full.")
        return None
    else:
        parking_slots[empty_slot] = time.time()
        print("Vehicle parked in slot", empty_slot+1)
        print("Entry time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(parking_slots[empty_slot])))
        return None
def unpark_vehicle():
    slot_number = input("Enter slot number of parked vehicle: ")
    slot_number = int(slot_number)-1
    if slot_number < 0 or slot_number >= num_slots:
        print("Invalid slot number. Please try again.")
        return None
    elif parking_slots[slot_number] == None:
        print("No vehicle found in slot", slot_number+1)
        return None
    else:
        entry_time = parking_slots[slot_number]
        exit_time = time.time()
        parking_slots[slot_number] = None
        parking_duration = exit_time - entry_time
        parking_cost = parking_duration * cost_per_hour / 3600
        print("Vehicle unparked from slot", slot_number+1)
        print("Exit time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(exit_time)))
        print("Parking duration: {:.2f} seconds".format(parking_duration))
        print("Parking cost: Rs. {:.2f}".format(parking_cost))
        return None
def display_status():
    print("Current status of parking lot:")
    for i in range(num_slots):
        if parking_slots[i] == None:
            print("Slot", i+1, "is empty")
        else:
            print("Slot", i+1, "is occupied by a vehicle parked at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(parking_slots[i])))
def main():
    while True:
        print("Please select an option:")
        print("1. Park a vehicle")
        print("2. Unpark a vehicle")
        print("3. Display current status")
        print("4. Exit")
        choice = input()
        if choice == "1":
            park_vehicle()
        elif choice == "2":
            unpark_vehicle()
        elif choice == "3":
            display_status()
        elif choice == "4":
            print("Thank you for using our parking lot!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
