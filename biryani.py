class Biryani:
    def __init__(self):
        self.color='brown'
        self.quantity='1packet'
    def smell(self):
        print("biryani smells good")
    def spicy(self):
        print('it is very spicy')
vin=Biryani()
print(vin.color)
print(vin.quantity)
vin.smell()
vin.spicy()
