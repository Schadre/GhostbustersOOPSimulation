import random

class Ghosts:
    ghostbusters_ghosts = {
        "Slimer": {
            "Scare Level": 5,
            "Weakness": "Proton Beams"
        },
        "Gozer the Gozerian": {
            "Scare Level": 10,
            "Weakness": "Crossing Proton Beams"
        },
        "Stay Puft Marshmallow Man": {
            "Scare Level": 10,
            "Weakness": "Being Roasted by Proton Beams"
        },
        "Zuul (The Gatekeeper)": {
            "Scare Level": 8,
            "Weakness": "Proton Beams"
        },
        "Vinz Clortho (The Keymaster)": {
            "Scare Level": 8,
            "Weakness": "Proton Beams"
        },
        "Library Ghost (Eleanor Twitty)": {
            "Scare Level": 10,
            "Weakness": "Loud environments"
        },
        "Terror Dogs": {
            "Scare Level": 5,
            "Weakness": "Proton Beams"
        },
        "Vigo the Carpathian": {
            "Scare Level": 9,
            "Weakness": "Happiness"
        },
        "Scoleri Brothers": {
            "Scare Level": 8,
            "Weakness": "Proton Beams"
        },
        "Titanic Passengers": {
            "Scare Level": 5,
            "Weakness": "Proton Beams"
        },
        "Jogger Ghost": {
            "Scare Level": 3,
            "Weakness": "Proton Beams"
        },
        "Muncher": {
            "Scare Level": 10,
            "Weakness": "Proton Beams"
        },
    }
    def __init__(self):
        ghost_name = random.choice(list(self.ghostbusters_ghosts.keys()))
        ghost_data = self.ghostbusters_ghosts[ghost_name]
        self.name = ghost_name
        self.scare_level = ghost_data["Scare Level"]
        self.weakness = ghost_data["Weakness"]


    def haunt(self):
        """Increases scare level"""
        self.scare_level += 2
        print(f"{self.name} scare level has significantly increased to {self.scare_level}!\n")
        print(f"{self.name} not able to be captured!")
        ghost_actions = ["The ghost has started fighting back!", "The ghost is running away!", "The Ghost is laughing at your weak attempts to capture it!"]
        print(f"{random.choice(ghost_actions)}")

    def react_to_weakness(self):
        """Ghost losing power by taking damage"""
        self.scare_level -=5
        print(f"\nThe ghost has been exposed to it's weakness {self.weakness} and it's scare level is now {self.scare_level}! Capture it now!\n")
