class Vehicle :
    def __init__(self, max_speed, mileague):
        self.max_speed = max_speed
        self.mileague = mileague

modelX = Vehicle(200,18)
print(modelX.max_speed, modelX.mileague)

