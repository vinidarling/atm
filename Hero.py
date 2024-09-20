class Hero:
    def __init__(self):
        self.color="brown"
        self.name="prabhas"
        self.height=6.1
        self.age=45
    def act(self):
        print('prabhas acted in salaar')
    def sleep(self):
        print('prabhas just slept')
v1=Hero()
print(v1.name)
print(v1.color)
print(v1.height)
v1.height=6.2
v1.color='white'
v1.mob=7998
v1.add='bhimavaram'
v2=v1
v3=v2
print(v3.name)
print(v2.color)
print(v1.height)
print(v3.mob)
print(v1.age)
print(v3.add)
v3.act()
v2.sleep()