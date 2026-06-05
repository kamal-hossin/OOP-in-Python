class Divice:
    def __init__(self, name, color, price, origin):
        self.name = name
        self.color = color
        self.price = price
        self.origin = origin


class Phone(Divice):
    def __init__(self, name, color, price, origin):
        super().__init__(name, color, price, origin)
        self.phone_name = name
        self.phone_color = color
        self.phone_price = price

class Laptop(Divice):
    def __init__(self, name, color, price, origin):
        super().__init__(name, color, price, origin)
        self.laptop_name = name
        self.laptop_color = color
        self.laptop_price = price

class Computer(Divice):
    def __init__(self, name, color, price, origin):
        super().__init__(name, color, price, origin)
        self.computer_name = name
        self.computer_color = color
        self.computer_price = price   


My_phone = Phone("iPhone", "Black", 1000, "USA")
print(f"Phone Name: {My_phone.phone_name}")
print(f"Phone Color: {My_phone.phone_color}")
print(f"Phone Price: {My_phone.phone_price}")

My_laptop = Laptop("MacBook Pro", "Silver", 2000, "USA")
print(f"Laptop Name: {My_laptop.laptop_name}")
print(f"Laptop Color: {My_laptop.laptop_color}")
print(f"Laptop Price: {My_laptop.laptop_price}")


My_computer = Computer("Dell XPS", "Black", 1500, "USA")
print(f"Computer Name: {My_computer.computer_name}") 
print(f"Computer Color: {My_computer.computer_color}")
print(f"Computer Price: {My_computer.computer_price}")                        