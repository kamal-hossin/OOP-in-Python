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


class Phone:
    def __init__(self, sim_type):
        self.sim_type = sim_type

    def show_phone_info(self):
        print(f"SIM Type : {self.sim_type}")


class Camera:
    def __init__(self, camera):
        self.camera = camera

    def show_camera_info(self):
        print(f"Camera   : {self.camera}")


# Multiple Inheritance
class SmartPhone(Device, Phone, Camera):
    def __init__(self, name, color, price, origin, sim_type, camera):

        Device.__init__(self, name, color, price, origin)
        Phone.__init__(self, sim_type)
        Camera.__init__(self, camera)


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
my_phone.show_camera_info()