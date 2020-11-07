class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.state = "main"

    def __str__(self):
        return f"""Coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money"""

    def fill(self, water_fill, milk_fill, coffee_fill, cups_fill):
        self.water += int(water_fill)
        self.milk += int(milk_fill)
        self.coffee += int(coffee_fill)
        self.cups += int(cups_fill)

    def make_coffee(self, water_for_coffee, milk_for_coffee, coffee_for_coffee, cups_for_coffee, money_for_coffee):
        if water_for_coffee > self.water:
            print("Sorry, not enough water!")
        elif milk_for_coffee > self.milk:
            print("Sorry, not enough milk!")
        elif coffee_for_coffee > self.coffee:
            print("Sorry, not enough coffee beans!")
        elif cups_for_coffee > self.cups:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_for_coffee
            self.milk -= milk_for_coffee
            self.coffee -= coffee_for_coffee
            self.cups -= cups_for_coffee
            self.money += money_for_coffee

    def buy(self, drink):
        if drink == "espresso":
            self.make_coffee(250, 0, 16, 1, 4)
        elif drink == "latte":
            self.make_coffee(350, 75, 20, 1, 7)
        elif drink == "cappuccino":
            self.make_coffee(200, 100, 12, 1, 6)

    def action(self, string):
        if self.state == "main":
            if string == "exit":
                self.state = False
            elif string == "remaining":
                print(self)
            elif string == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif string == "buy":
                self.state = "buy"
            elif string == "fill":
                self.state = "fill"
        elif self.state == "buy":
            if string == "back":
                self.state = "main"
            elif string == "1":
                self.buy("espresso")
            elif string == "2":
                self.buy("latte")
            elif string == "3":
                self.buy("cappuccino")


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while coffee_machine.state:
    if coffee_machine.state == "main":
        initial_string = input("Write action (buy, fill, take, remaining, exit):")
        coffee_machine.action(initial_string)
    if coffee_machine.state == "buy":
        initial_string = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_machine.action(initial_string)
        coffee_machine.state = "main"
    if coffee_machine.state == "fill":
        fill_water = input("Write how many ml of water do you want to add:")
        fill_milk = input("Write how many ml of milk do you want to add:")
        fill_coffee = input("Write how many grams of coffee beans do you want to add:")
        fill_cups = input("Write how many disposable cups of coffee do you want to add:")
        coffee_machine.fill(fill_water, fill_milk, fill_coffee, fill_cups)
        coffee_machine.state = "main"
