class Tv:
    def __init__(self):
        self.color='black'
        self.cost=77777
v1=Tv()
v3=v1
print(v1)
print(v3)
print(id(v1))
print(id(v3))
print(v1 is v3)