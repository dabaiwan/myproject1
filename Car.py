class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        self.print_state()

    def print_state(self):
        print("I'm going {} kph".format(self.speed))
