class Saipallavi:
    def __init__(self):
        self.height=5.7
        self.color=('red')
        self.age=33
        self.industry='malayalam'
    def cry(self):
        print('pallavi cried at padi padi leche manasu movie ')
    def dance(self):
        print("she did great dance with chai")
p1=Saipallavi()
print(p1.industry)
print(p1.color)
print(p1.age)
print(p1.height)
p1.age=32
p1.profession='actress'
p2=p1
v3=p2
print(v3.profession)
print(p2.color)
print(p2.age)
print(p1.age)
print(v3.height)
print(v3.industry)
v3.cry()
p2.dance()