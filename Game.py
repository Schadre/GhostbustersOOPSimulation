from Classes.ContainmentUnit import ContainmentUnit
from Classes.Equipment import EctoGoggles, Equipment, GhostTrap, ProtonPack
from Classes.Ghost import Ghosts
from Classes.GhostBuster import Ghostbusters

containment = ContainmentUnit()
equipments = Equipment("Type of Equipment", 5, 5)
ghosts = Ghosts()
ghostbusters = Ghostbusters("Full Name", "Equipment", 10)
equipments_1 = ProtonPack()
equipments_2 = GhostTrap(containment)
equipments_3 = EctoGoggles()

def game():
    while True:
        print("\nWelcome to the Ghostbusters Game Simulation")
        print("\nMain Menu:\n")
        menu = input(" 1. Enter the 'Containment Unit'\n 2. Check out the 'Equipment'\n 3. Interact with the 'Ghosts'\n 4. Join the 'Ghostbusters'\n 5. Exit\n")
        try:
            if menu == "1":
                print("\nWelcome to the Containtment Unit")

                containment_choices = input("\n 1. Add Ghost into the 'Containment Unit\n 2. Display Ghost inside the 'Containtment Unit'\n 3. Find out which ghost has escaped!\n 4. Exit\n")
                if containment_choices == "1":
                    name = input("Please enter the name of the ghost: ")
                    scare_level = int(input("Please enter the scare levelof the ghost(numbers only): "))
                    weakness = input("Please enter the weakness of the ghost: ")
                    containment.add_ghost(name, scare_level, weakness)
                elif containment_choices == "2":
                    containment.display_ghost()
                elif containment_choices == "3":
                    containment.escaped_ghost()
                elif containment_choices == "4":
                    break
                else:
                    print("Invalid choice, please try again.")

            elif menu == "2":
                print("\nWelcome to the Equipment Collection")

                equipment_choices = input("\n 1. View Equipment\n 2. Upgrade Equipment\n 3. Exit\n")
                if equipment_choices == "1":
                    equipments.view_equipment()
                elif equipment_choices == "2":
                    equipments_type = input("Please select the equipment you would like to upgrade: \n 1. Proton Pack\n 2. GhostTrap\n 3. EctoGoggles \n")
                    if equipments_type == "1":
                        equipments_1.upgrade_equipment(ProtonPack())
                    elif equipments_type == "2":
                        equipments_2.upgrade_equipment(GhostTrap("Any"))
                    elif equipments_type == "3":
                        equipments_3.upgrade_equipment(EctoGoggles())
                    else:
                        print("Invalid choice, please try again.")
                elif equipment_choices == "3":
                    break
                else:
                    print("Invalid choice, please try again.")

            elif menu == "3":
                print("\nWelcome to the world of Ghost!")

                ghost_hunting = input("\n 1. Explore \n 2. Scan the area \n 3. Exit\n")
                if ghost_hunting == "1":
                    ghosts.haunt()
                    ghosts_choice = input("\n What would you like to do?\n 1. Fight\n 2. Run\n 3. Exit\n")
                    if ghosts_choice == "1":
                        equipments_1.attack_ghost()
                        ghosts.react_to_weakness()
                        equipments_2.capture_ghost(ghosts.name, ghosts.scare_level, ghosts.weakness)
                    elif ghosts_choice == "2":
                            equipments_3.scan_for_ghost()
                            print(f"After seeing the additional ghost, you run for your life!!")
                            break
                    elif ghosts_choice == "3":
                        break
                    else:
                        print("Invalid choice, please try again.")
                elif ghost_hunting == "2":
                    equipments_3.scan_for_ghost()
                elif ghost_hunting == "3":
                    break
                else:
                    print("Invalid choice, please try again.")

            elif menu == "4":

                print("\nJoin the 'Ghostbusters' today!")
                joining = input("\n 1. Join Our Team\n 2. See our current Ghostbusters!\n 3. Find an individual ghostbuster by name\n 4. Train for fighting ghost\n 5. Exit\n")
                if joining == "1":
                    name = input("Please enter your full name: ").title()
                    equipment_pick = input(" Please pick a weapon:: \n 1. Proton Pack\n 2. Ghost Trap\n 3. EctoGoggles \n")
                    if equipment_pick == "1":
                        equipment = "Proton Pack"
                    elif equipment_pick == "2":
                        equipment = "Ghost Trap"
                    elif equipment_pick == "3":
                        equipment = "Ecto Goggles"
                    else:
                        print("Invalid choice, please try again.")
                    skill_level = int(input("Please enter your skill level for hunting ghost(numbers only): "))
                    ghostbusters.add_ghostbuster(name, equipment, skill_level)
                elif joining == "2":
                    ghostbusters.list_all_ghostbusters()
                elif joining == "3":
                    name = input("Please enter the full name of the ghostbuster:\n ").title()
                    ghostbusters.display_ghostbuster(name)
                elif joining == "4":
                    name = input("Please enter the full name of the ghostbuster for training:\n ").title()
                    ghostbusters.train_for_ghost(name)
                elif joining == "5":
                    break
                else:
                    print("Invalid choice, please try again.")

            elif menu == "5":
                print("\nGoodbye ^_^")
                break
            else:
                print("Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    game()
