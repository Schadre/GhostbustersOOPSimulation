from Classes.ContainmentUnit import ContainmentUnit
from Classes.Ghost import Ghosts
import random

ghosts = Ghosts()

class Equipment: 
    def __init__(self, type, power, durability):
        self.type = type
        self.power = power
        self.durability = durability
    
    def view_equipment(self):
        equipment_list = ["Proton Pack", "Ghost Trap", "Ecto Goggles"]
        print("\nHere is a list of equipment available: \n")
        for items in equipment_list:
            print(f" {items}")
    
    def upgrade_equipment(self, type):
        """Increase the equipment power and durability"""
        self.power +=1 
        self.durability +=1 
        print(f"The total power and durability has been increased for {self.type}!")
        print(f" Current power: {self.power}")
        print(f" Current Durability: {self.durability}")

class ProtonPack(Equipment):
    def __init__(self):
        super().__init__("Proton Pack", 5, 5)

    def attack_ghost(self):
        """Using the proton pack to attack ghost"""
        print("The ghost has been hit with a beam ray from your proton pack!")

class GhostTrap(Equipment):
    def __init__(self, containment_unit):
        super().__init__("Ghost Trap", 5, 5)
        self.containment_unit = containment_unit

    def capture_ghost(self, ghost_name, scare_level, weakness):
        """Using the Ghost Trap to capture ghost and add them to the containment unit module"""
        print(f"{ghost_name} has been successfully captured! ")
        self.containment_unit.add_ghost(ghost_name, scare_level, weakness)
        
class EctoGoggles(Equipment):
    def __init__(self):
        super().__init__("Ecto Goggles", 5, 5)

    def scan_for_ghost(self):
        """Using the Ecto Goggles Equipment to find ghost"""
        print("Scanning for ghost in the area...\n")
        amount_of_ghost = list(range(1, 16))
        print(f"\nThe Ecto Goggles has located: {random.choice(amount_of_ghost)} ghost!\n")



