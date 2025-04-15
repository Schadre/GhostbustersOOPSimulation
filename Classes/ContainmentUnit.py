import random

class ContainmentUnit():
    def __init__(self):
        self.capacity = 10000
        self.ghost_stored = 0
        self.EctoContainmentUnit = {}

    def add_ghost(self, name, scare_level, weakness):
        "Adding ghost to the containment unit"
        if name not in self.EctoContainmentUnit:
            if self.ghost_stored <= self.capacity:
                self.ghost_stored += 1
                self.EctoContainmentUnit[name] = {
                    "Scare Level" : scare_level,
                    "Weakness" : weakness,
                    "Captured" : True
                }
                print(f"{name} has been placed inside of the Containment unit.")
            else:
                print("Warning the containment unit has reached maximum capacity")
        else:
            print("This ghost has already been placed in the unit, it must have escaped when we weren't looking!")

    def display_ghost(self):
        """Show all current ghost in the containment unit"""
        print(f"\nThe Ecto Containment Unit currently holds: {self.ghost_stored} Ghost")
        for name, details in self.EctoContainmentUnit.items():
            print(f"\nDetailed Ghost information: \n Name: {name}\n Scare Level: {details["Scare Level"]}\n Weakness: {details["Weakness"]}\n Captured: {details["Captured"]}\n")

    def escaped_ghost(self):
        """Powerful ghost escaping at random"""
        try:
            name = random.choice(list(self.EctoContainmentUnit.keys()))
            if self.EctoContainmentUnit[name]["Scare Level"] >= 5 and self.EctoContainmentUnit[name]["Captured"] == True:
                print(f"Oh no! {name} has escaped the containment unit!")
            else:
                print("Luckily, no ghost have escaped!")
        except Exception as e:
            print(f"An error ocurred: {e}")

