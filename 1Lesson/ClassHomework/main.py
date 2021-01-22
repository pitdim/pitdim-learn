class Means_of_transportation():

    sound = "пиу пиу"

    def __init__(self, l_oil):
        self.l_oil = l_oil

    def PlaySound(self):
        print("транспорт издал звук:", self.sound)

class Car(Means_of_transportation):
    def __init__(self, wheel):
        self.wheel = wheel
        self.l_oil = l_oil



class LegkovoyCar(Car):
    sound = "вррр..."
    def __init__(self, wheel,l_oil):
        self.wheel = wheel
        self.l_oil = l_oil
    def StartCar(self):
        if self.l_oil <= 0:
            raise ValueError("Топлива нет, не получилось начать движение.")
        else:
            print("началось движение....")
    def PlaySound(self):
        print("Машина издала звук:", self.sound)


f = LegkovoyCar(4, 1)
f.StartCar()
f.PlaySound()


class Boat(Means_of_transportation):
    pass

class Motor_boat(Boat):
    sound = "бульк бульк"
    def __init__(self, oil, speed):
        self.oil = oil
        self.speed = speed




h = Motor_boat(20, 30)
h.PlaySound()
