import pickle
from collections import deque
from datetime import datetime

TOTAL_SLOTS = 5
parking_slots = [None] * TOTAL_SLOTS
waiting_queue = deque()
history_stack = []

class Vehicle:
    def __init__(self, number, entry_time):
        self.number = number
        self.entry_time = entry_time

def save_data():
    with open("parking_data.pkl", "wb") as f:
        pickle.dump((parking_slots, list(waiting_queue)), f)

def load_data():
    global parking_slots, waiting_queue
    try:
        with open("parking_data.pkl", "rb") as f:
            parking_slots, q = pickle.load(f)
            waiting_queue = deque(q)
    except FileNotFoundError:
        pass

def add_vehicle():
    number = input("Enter vehicle number: ")
    entry_time = datetime.now()
    vehicle = Vehicle(number, entry_time)
    if None in parking_slots:
        slot = parking_slots.index(None)
        parking_slots[slot] = vehicle
        print(f"✅ Vehicle {number} parked at slot {slot+1}")
        history_stack.append(("add", slot))
    else:
        waiting_queue.append(vehicle)
        print(f"⏳ No slots free. Vehicle {number} added to waiting queue.")

def remove_vehicle():
    number = input("Enter vehicle number to remove: ")
    for i in range(TOTAL_SLOTS):
        if parking_slots[i] and parking_slots[i].number == number:
            entry_time = parking_slots[i].entry_time
            parked_hours = (datetime.now() - entry_time).seconds // 3600 + 1
            fee = parked_hours * 20
            print(f"🚗 Vehicle {number} removed from slot {i+1}. Fee: ₹{fee}")
            parking_slots[i] = None
            history_stack.append(("remove", i))
            if waiting_queue:
                next_vehicle = waiting_queue.popleft()
                parking_slots[i] = next_vehicle
                print(f"✅ Vehicle {next_vehicle.number} assigned to slot {i+1}")
            return
    print("❌ Vehicle not found in parking lot.")

def display_parking():
    print("\n📋 Parking Lot Status:")
    for i, slot in enumerate(parking_slots):
        if slot:
            print(f"Slot {i+1}: {slot.number} (since {slot.entry_time.strftime('%H:%M:%S')})")
        else:
            print(f"Slot {i+1}: Empty")
    print()

def available_slots():
    free = parking_slots.count(None)
    print(f"🅿️ Available slots: {free}/{TOTAL_SLOTS}")

def search_vehicle():
    number = input("Enter vehicle number to search: ")
    for i, slot in enumerate(parking_slots):
        if slot and slot.number == number:
            print(f"🔎 Vehicle {number} found at slot {i+1}")
            return
    print("❌ Vehicle not found.")

def main():
    load_data()
    while True:
        print("\n===== 🚗 Smart Parking Lot Menu =====")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Display Parking Slots")
        print("4. Show Available Slots")
        print("5. Search Vehicle")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            display_parking()
        elif choice == "4":
            available_slots()
        elif choice == "5":
            search_vehicle()
        elif choice == "6":
            save_data()
            print("💾 Data saved. Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()

