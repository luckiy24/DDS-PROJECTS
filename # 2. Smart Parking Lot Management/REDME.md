# 🚗 Smart Parking Lot Management System

## 📌 Overview
**The Smart Parking Lot Management System** is a project that manages vehicle entry and exit in a parking lot efficiently. It keeps track of available slots, assigns parking spaces automatically, and maintains vehicle details like number plate, slot, and time of entry. The system helps simulate real-world smart parking management.

---
## 🛠 Features
- Add a vehicle (auto-assign nearest free slot)
- Remove a vehicle (free the slot & calculate charges)
- Display all parked vehicles with slot details
- Show available slots in the parking lot
- Search for a vehicle by number plate
- Maintain a waiting queue if slots are full
- Save & load parking records from a file

---
## 📂 Data Structures Used
- Array / List of Structures → To represent parking slots and store vehicle details
- Queue → To manage waiting vehicles when parking is full
- Stack → To implement undo/redo of last parking operation (optional feature)
- File Handling → To save parking records for future use

---
## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/your-username/smart-parking-lot.git
cd smart-parking-lot/src

# Run the program
python parking_lot.py
