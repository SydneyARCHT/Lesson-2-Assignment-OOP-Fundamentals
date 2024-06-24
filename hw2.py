# Lesson 2: Assignment | OOP Fundamentals
# 1. City Infrastructure Management System
# Task 1: Vehicle Registration System

class Vehicle:

    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner


    def update_owner(self, new_owner):
        self.owner = new_owner
        return (f"{type} is now registered to {new_owner}")
    

def main():
    while True:
        vehicle = Vehicle("12345", "Truck", "Ricky")
        print(f"Current owner of {vehicle.registration_number} {vehicle.type}: {vehicle.owner}")
        new_owner = input("Who is the vehicle being transferred to? ")
        vehicle.update_owner(new_owner)
        print(f"New owner of {vehicle.registration_number} {vehicle.type} is {vehicle.owner}")



# Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.count = 0
    

    def add_participant(self):
        self.count += 1


    def get_participant_count(self):
        return self.count
    
