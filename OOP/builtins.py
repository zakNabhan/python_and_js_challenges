class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def print_data(self):
        print(self.make)
        print(self.price)

    def switch_on(self):
        self.on = True


kenwood = Kettle("kenwood", 9.88)
#print(kenwood.print_data())
print("models: {} = {}".format(kenwood.make, kenwood.price))
print("models: {0.make} = {0.price}".format(kenwood))

Kettle.switch_on(kenwood)
print(kenwood.on)