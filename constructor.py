class Phone:
    phone_name= "iPhone"
    phone_color= "Black"
    phone_price= 1000

    def __init__(self, name, color, price):
        self.phone_name = name
        self.phone_color = color
        self.phone_price = price

My_phone= Phone("iPhone", "Black", 1000);
print(My_phone.phone_name)
print(My_phone.phone_color)
print(My_phone.phone_price)