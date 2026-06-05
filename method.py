class Phone:
    phone_name= "iPhone"
    phone_color= "Black"
    phone_price= 1000
    phone_features= "Face ID, Wireless Charging, Water Resistant , Cemera"

    def phone_info(self):
        return f"{self.phone_name} has {self.phone_features} and costs {self.phone_price}"
    
My_phone= Phone();
print(My_phone.phone_info());