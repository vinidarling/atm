class Student:
    def __init__(self):
        self.name='prabhas'
        self.id=2010121
        self.address='sadum'
        self.favoritenumber=7
    def watch(self):
        print('prabhas watching match')
    def eat(self):
        print('prabhas ate eggrice just now')
s1=Student()
print(s1.name)
print(s1.id)
print(s1.address)
print(s1.favoritenumber)
s1.watch()
s1.eat()