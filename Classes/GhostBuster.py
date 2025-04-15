class Ghostbusters:
    def __init__(self, name, equipment, skill_level):
        self.name = name
        self.equipment = equipment
        self.skill_level = skill_level
        self.ghostbusters = {
            "Egon Spengler" : {
                "Equipment" : "Proton Pack",
                "Skill Level" : 10,
            },
            "Dr. Peter Venkman" : {
                "Equipment": "Proton Pack",
                "Skill Level": 10,
            },
            "Winston Zeddemore" : {
                "Equipment": "Proton Pack",
                "Skill Level": 10,
            },
            "Ray Stantz" : {
                "Equipment": "Proton Pack",
                "Skill Level": 10,
            },
            "Louis Tully" : {
                "Equipment": "Proton Pack",
                "Skill Level": 2,
            },
        }

    def add_ghostbuster(self, name, equipment, skill_level):
        """Adding ghostbusters to the database"""
        self.ghostbusters[name] = {
            "Equipment": equipment,
            "Skill Level": skill_level
        }
        print(f"{name} has been added to our Ghostbusters team!")

    def display_ghostbuster(self, name):
        """Display individual Ghostbusters information"""
        if name in self.ghostbusters:
            print(f"\nDetailed Ghostbuster information:\n Name: {name}\n Equipment: {self.ghostbusters[name]["Equipment"]}\n Skill Level: {self.ghostbusters[name]["Skill Level"]}\n")
        else:
            print(f"{name} is not on our Ghostbusters Team.")
    
    def list_all_ghostbusters(self):
        """Display all Ghostbusters in the system"""
        for name, details in self.ghostbusters.items():
            print(f"\nDetailed Ghostbuster information:\n Name: {name}\n Equipment: {details["Equipment"]}\n Skill Level: {details["Skill Level"]}\n")

    def train_for_ghost(self, name):
        """Increasing the skill level to fight stronger ghost"""
        try:
            self.ghostbusters[name]["Skill Level"] += 1 
            print(f"{name} skill level has increased with training! Keep up the great work. Soon enough, you will capture ghost at all scare levels!")
        except KeyError as e:
            print(f"The name {e} is not found")
