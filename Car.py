class Car:
    def __init__(self, speed=0,name=""):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.name = name

    def say_speed(self):
        self.print_state()

    def print_state(self):
        print("I'm going {} kph".format(self.speed))

    def say_name(self):
        print("{}".format(self.name))
