"""
OOP Assignment
---------------
This program demonstrates core Object-Oriented Programming (OOP) concepts:
1. Class design with attributes, methods, constructors, inheritance, and encapsulation.
2. Polymorphism using different classes implementing the same method in unique ways.
"""

# -----------------------------
# Assignment 1: Design Your Own Class 🏗️
# -----------------------------

class Device:
    """Parent class representing a generic device."""
    
    def __init__(self, brand, model):
        """Constructor to initialize device attributes."""
        self.brand = brand
        self.model = model
    
    def device_info(self):
        """Return the device information."""
        return f"{self.brand} {self.model}"
    

class Smartphone(Device):
    """Child class inheriting from Device, representing a Smartphone."""
    
    # Encapsulation: private attribute (not directly accessible outside class)
    __battery_health = 100
    
    def __init__(self, brand, model, os, storage):
        """
        Constructor to initialize smartphone attributes.
        Calls the parent Device constructor for brand and model.
        """
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
    
    def make_call(self, number):
        """Simulate making a phone call."""
        return f"📞 Calling {number} using {self.device_info()}..."
    
    def check_storage(self):
        """Check available storage."""
        return f"💾 {self.storage} GB available"
    
    def get_battery_health(self):
        """Access the private battery health attribute safely."""
        return f"🔋 Battery health: {self.__battery_health}%"
    
    def use_battery(self, amount):
        """Reduce battery health by a given amount, but not below 0."""
        self.__battery_health -= amount
        if self.__battery_health < 0:
            self.__battery_health = 0
        return f"⚡ Battery health now: {self.__battery_health}%"


# Create smartphone objects
phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)

# Demonstrate Smartphone class functionality
print("=== Assignment 1 Output ===")
print(phone1.make_call("+123456789"))
print(phone2.check_storage())
print(phone1.get_battery_health())
print(phone1.use_battery(20))


# -----------------------------
# Activity 2: Polymorphism Challenge 🎭
# -----------------------------

class Animal:
    """Base class representing a generic animal."""
    def move(self):
        return "This animal moves somehow"

class Dog(Animal):
    """Dog class inheriting from Animal, overrides move()."""
    def move(self):
        return "🐕 Running on 4 legs"

class Bird(Animal):
    """Bird class inheriting from Animal, overrides move()."""
    def move(self):
        return "🕊️ Flying in the sky"

class Fish(Animal):
    """Fish class inheriting from Animal, overrides move()."""
    def move(self):
        return "🐟 Swimming in water"


# Demonstrate polymorphism
print("\n=== Activity 2 Output ===")
animals = [Dog(), Bird(), Fish()]
for a in animals:
    print(a.move())
