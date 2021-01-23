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
    def __init__(self, wheel,l_oil, speed):
        self.wheel = wheel
        self.l_oil = l_oil
        self.speed = speed

    def StartCar(self):
        if self.l_oil <= 0:
            raise ValueError("Топлива нет, не получилось начать движение.")
        if self.wheel < 4:
            raise ValueError("Вы дали машине мало колес, не хватает КОЛЕС!!")
            exit(0)
        if self.speed <= 0:
            raise ValueError("Ваша машина не тронется с мизерной скоростью...")
            exit(0)
        else:
            print("началось движение....")


    def PlaySound(self):
        print("Машина издала звук:", self.sound)
class Boat(Means_of_transportation):
    pass
class Motor_boat(Boat):
    sound = "бульк бульк"
    go_on_water = True
    def __init__(self, oil, speed, go_on_water):
        self.oil = oil
        self.speed = speed
        self.go_on_water = go_on_water
    def StartMotorBoat(self):
        if self.go_on_water != True:
            raise ValueError("Вы указали то что лодка не ходит по воде :З , не получилось начать движение.")
            exit(0)
        if self.oil <= 0:
            raise ValueError("Топлива нет , не получилось начать движение.")
            exit(0)
        if self.speed <= 0:
            raise ValueError("Ваша лодка не тронется с мизерной скоростью...")
            exit(0)
        else:
            print("началось движение....")
class Samolet(Means_of_transportation):
    pass
class PassagirniySamolet(Samolet):
    sound = "фью фью..."
    motor = True
    def __init__(self, s_oil, speed, motor):
        self.s_oil = s_oil
        self.speed = speed
        self.motor = motor

    def StartPassagirsliySamolet(self):
        if self.motor != True:
            raise ValueError("Мотора нет :( , не получилось начать движение.")
            exit(0)
        if self.s_oil <= 0:
            raise ValueError("Топлива нет, не получилось начать движение.")
            exit(0)
        if self.speed <= 0:
            raise ValueError("Ваш самолет не тронется с мизерной скоростью...")
            exit(0)
        else:
            print("началось движение....")




ExemplyarLegkovoyCar = LegkovoyCar(4, 100, 120)
print("Скорость легковой машины равна", ExemplyarLegkovoyCar.speed,"км/ч")
print("Количевство колес у легковой машины равно", ExemplyarLegkovoyCar.speed)
print("Количевство топлива в баке легковой машины равна", ExemplyarLegkovoyCar.l_oil,"литров.")
ExemplyarLegkovoyCar.PlaySound()
ExemplyarLegkovoyCar.StartCar()

print("--------" * 10)
ExemplyarMotorBoat = Motor_boat(20, 60, True)
print("Скорость моторной лодки равна", ExemplyarMotorBoat.speed,"км/ч")
print("Количевство топлива в моторной лодке равно -", ExemplyarMotorBoat.oil,"литров.")
print("Есть ли у нашей моторной лодки мотор? -", ExemplyarMotorBoat.go_on_water)
ExemplyarMotorBoat.PlaySound()
ExemplyarMotorBoat.StartMotorBoat()

print("--------" * 10)
ExemplyarPassagirskiySamolet = PassagirniySamolet(300, 500, True)
print("Скорость пассажирскоо самолета равна", ExemplyarPassagirskiySamolet.speed,"км/ч")
print("Количевство топлива в пассажирском самолете равно -", ExemplyarPassagirskiySamolet.s_oil,"литров.")
print("Есть ли у нашего пассажирского самолета мотор? -", ExemplyarPassagirskiySamolet.motor)
ExemplyarPassagirskiySamolet.PlaySound()
ExemplyarPassagirskiySamolet.StartPassagirsliySamolet()