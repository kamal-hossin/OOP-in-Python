class Payment:

    def pay(self):
        print("Payment Processing...")


class Bkash(Payment):

    def pay(self):
        print("Payment done using Bkash")


class Nagad(Payment):

    def pay(self):
        print("Payment done using Nagad")


class Rocket(Payment):

    def pay(self):
        print("Payment done using Rocket")


# Object Create
bkash = Bkash()
nagad = Nagad()
rocket = Rocket()


# Polymorphism
bkash.pay()
nagad.pay()
rocket.pay()