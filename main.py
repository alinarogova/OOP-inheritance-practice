class Device:
    def __init__(self, power, weight, height, type_):
        self.power = power
        self.weight = weight
        self.height = height
        self.type = type_
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.type} turns on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.type} turns off.")


class CoffeeMachine(Device):
    def __init__(self, power, weight, height, type_):
        super().__init__(power, weight, height, type_)
        self.resources = {
           "water": 300,
           "milk": 200,
           "coffee": 100,
        }
        self.capacity = {
            "water": 1000,
            "milk": 400,
            "coffee": 200,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink:
            if drink[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def add_resources(self, res):
        for item in self.resources:
            self.resources[item] += res[item]

    def __make_coffee(self, order, coffe_type):
        if not self.is_on:
            print("Turn on your device.")
        elif self.is_resource_sufficient(order):
            for item in order:
                self.resources[item] -= order[item]
            print(f"Here's your {coffe_type}. Enjoy!")

    def make_cappuccino(self):
        order = {
           "water": 50,
           "milk": 20,
           "coffee": 5,
        }
        self.__make_coffee(order, coffe_type='cappuccino')

    def make_latte(self):
        order = {
            "water": 70,
            "milk": 40,
            "coffee": 5,
        }
        self.__make_coffee(order, coffe_type='latte')

    def make_americano(self):
        order = {
            "water": 30,
            "milk": 0,
            "coffee": 10,
        }
        self.__make_coffee(order, coffe_type='americano')


class Blender(Device):
    def __init__(self, power, weight, height, type_, *args):
        super().__init__(power, weight, height, type_)
        self.ingredients = [e for e in args]
        self.speed = 0
        self.is_blended = False

    def add_ingredients(self, *args):
        if len(args) > 0:
            self.ingredients.extend(args)
            print(f"The ingredient(s) {', '.join(args)} added.")
        else:
            print("Nothing adds.")

    def set_speed(self, speed):
        if 0 <= speed <= 5:
            self.speed = speed
        else:
            print(f"The value {speed} is incorrect. Try again and set the integer between 0 and 5.")

    def blend(self):
        if self.is_blended:
            print("You have already made blend.")
        elif not self.is_on:
            print("You blender is off.")
        elif self.speed == 0:
            print("The blender can't work with speed = 0.")
        elif len(self.ingredients) == 0:
            print("The blender is empty.")
        else:
            print(f"Your blend from {', '.join(self.ingredients)} have just done!")
            self.is_blended = True

    def get_result(self):
        if self.is_blended:
            self.ingredients.clear()
            print("Enjoy the result!")
        else:
            print("Your blend haven't done!")

    def print_ingredients(self):
        print("Now you put in the blender: ", ', '.join(self.ingredients), ".", sep='')


class MeatGrinder(Device):
    def __init__(self, power, weight, height, type_, current_load=0):
        super().__init__(power, weight, height, type_)
        self.max_capacity = 3
        self.current_load = current_load

    def __str__(self):
        on_of = "on." if self.is_on else "off."
        return (f"Your meat grinder max_capacity is {self.max_capacity}. "
                f"You have already loaded {self.current_load}kg. "
                f"Your meat grinder is {on_of}")

    def add_meat(self, weight):
        if self.current_load + weight > self.max_capacity:
            print("You can't put so much meat.")
        else:
            self.current_load += weight

    def grid(self):
        if not self.is_on:
            print("Turn on your device, please.")
        elif self.current_load == 0:
            print("Nothing to grid.")
        else:
            print("Your device has worked successful.")
            self.current_load = 0


print("CoffeeMachine".center(60, "="))
coffee_machine = CoffeeMachine(1200, 3, 80, "Coffee Machine")
coffee_machine.add_resources({"water": 100, "coffee": 50, "milk": 20})
coffee_machine.make_americano()
coffee_machine.turn_on()
coffee_machine.make_americano()
coffee_machine.report()
coffee_machine.make_latte()
coffee_machine.make_latte()
coffee_machine.make_latte()
coffee_machine.make_cappuccino()
coffee_machine.report()
coffee_machine.make_cappuccino()
coffee_machine.make_cappuccino()
coffee_machine.make_cappuccino()
coffee_machine.report()
coffee_machine.add_resources({"water": 100, "coffee": 0, "milk": 0})
coffee_machine.make_latte()
print("\n", "Blender".center(60, "="), sep='')
blender = Blender(1200, 2, 60, "Blender", 'apple', 'banana')
blender.get_result()
blender.add_ingredients("strawberries", "pear")
blender.print_ingredients()
blender.blend()
blender.turn_on()
blender.set_speed(2)
blender.blend()
blender.get_result()
print("\n", "Meat Grinder".center(60, "="), sep='')
meatgrinder = MeatGrinder(1200, 4, 100, "MeatGrinder")
print(meatgrinder)
meatgrinder.grid()
meatgrinder.turn_on()
meatgrinder.grid()
meatgrinder.add_meat(0.9)
print(meatgrinder)
meatgrinder.grid()
print(meatgrinder)

print("Task 2".center(60, "="))


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


frigate = Frigate("Fregate-1", 3000, 150, 5)
frigate.sail()
frigate.attack()
frigate.launch_missile()

destroyer = Destroyer("Destroyer-1", 5000, 200, 10)
destroyer.sail()
destroyer.launch_torpedo()

cruiser = Cruiser("Cruiser-1", 10000, 300, 3)
cruiser.attack()
cruiser.launch_aircraft()

print("Task 3".center(60, "="))


class Money:
    def __init__(self, money, penny):
        self.money = money
        self.penny = penny
        self.__normalize()

    def __add__(self, other):
        money = self.money + other.money
        penny = self.penny + other.penny
        return Money(money, penny)

    def __str__(self):
        penny = str(self.penny) if self.penny > 9 else "0"+str(self.penny)
        return f"{self.money}.{penny}"

    def __normalize(self):
        self.money = self.money + self.penny//100
        self.penny = self.penny % 100


balance1 = Money(30, 789)
print(balance1)
balance2 = Money(78, 36)
balance3 = balance1+balance2
print(f"{balance1}+{balance2}={balance3}")
