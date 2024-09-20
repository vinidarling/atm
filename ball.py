class Ball:
    def __init__(self):
        self.brand='vini'
        self.color='yellow'
        self.cost=250
    def rotate(self):
        print("when bowler bowl a ball it rotates to reach the batsman")
    def bounce(self):
        print("when fielder throws the ball to keeper the ball went to him in one bounce")
v1=Ball()
print(v1.brand)
print(v1.cost)
print(v1.color)
v1.rotate()
v1.bounce()