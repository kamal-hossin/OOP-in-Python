class Device:
    def __init__(self, name, color, price, origin):
        self.name = name
        self.color = color
        self.price = price
        self.origin = origin

    def show_device_info(self):
        print("=== Device Information ===")
        print(f"Name   : {self.name}")
        print(f"Color  : {self.color}")
        print(f"Price  : {self.price}")
        print(f"Origin : {self.origin}")


# Device -> Phone
class Phone(Device):
    def __init__(self, name, color, price, origin, sim_type):
        super().__init__(name, color, price, origin)
        self.sim_type = sim_type

    def show_phone_info(self):
        print(f"SIM Type : {self.sim_type}")


# Device -> Phone -> SmartPhone
class SmartPhone(Phone):
    def __init__(self, name, color, price, origin, sim_type, camera):
        super().__init__(name, color, price, origin, sim_type)
        self.camera = camera

    def show_smartphone_info(self):
        print(f"Camera   : {self.camera}")


# Object Create
my_phone = SmartPhone(
    "iPhone 15 Pro",
    "Black",
    1500,
    "USA",
    "Dual SIM",
    "48 MP"
)

# Accessing all methods
my_phone.show_device_info()
my_phone.show_phone_info()
my_phone.show_smartphone_info()