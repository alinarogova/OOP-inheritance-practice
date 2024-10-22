class Ship:
    def __init__(self, name: str, displacement: int, firepower: int):
        self.name = name
        self.displacement = displacement  # Displacement (tons)
        self.firepower = firepower  # Firepower

    def sail(self):
        print(f"The ship {self.name} is sailing!")

    def attack(self):
        print(f"The ship {self.name} is attacking with firepower {self.firepower}!")


class Frigate(Ship):
    def __init__(self, name: str, displacement: int, firepower: int, missile_count: int):
        super().__init__(name, displacement, firepower)
        self.missile_count = missile_count

    def launch_missile(self):
        if self.missile_count > 0:
            self.missile_count -= 1
            print(f"Frigate {self.name} launches a missile! Missiles left: {self.missile_count}.")
        else:
            print(f"Frigate {self.name} has no missiles left!")


class Destroyer(Ship):
    def __init__(self, name: str, displacement: int, firepower: int, torpedo_count: int):
        super().__init__(name, displacement, firepower)
        self.torpedo_count = torpedo_count  # Number of torpedoes on board

    def launch_torpedo(self):
        if self.torpedo_count > 0:
            self.torpedo_count -= 1
            print(f"Destroyer {self.name} launches a torpedo! Torpedoes left: {self.torpedo_count}.")
        else:
            print(f"Destroyer {self.name} has no torpedoes left!")


class Cruiser(Ship):
    def __init__(self, name: str, displacement: int, firepower: int, aircraft_count: int):
        super().__init__(name, displacement, firepower)
        self.aircraft_count = aircraft_count  # Number of aircraft on board

    def launch_aircraft(self):
        if self.aircraft_count > 0:
            self.aircraft_count -= 1
            print(f"Cruiser {self.name} launches an aircraft! Aircraft left: {self.aircraft_count}.")
        else:
            print(f"Cruiser {self.name} has no aircraft left!")


frigate = Frigate("Fregat-1", 3000, 150, 5)
frigate.sail()
frigate.attack()
frigate.launch_missile()

destroyer = Destroyer("Destroyer-1", 5000, 200, 10)
destroyer.sail()
destroyer.launch_torpedo()

cruiser = Cruiser("Cruiser-1", 10000, 300, 3)
cruiser.attack()
cruiser.launch_aircraft()