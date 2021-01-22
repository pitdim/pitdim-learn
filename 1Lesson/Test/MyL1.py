class K1:

    def __init__(self):
        self.a = 1
        self.b = 500

    def __eq__(self, other):
        return self.a == other.a


class K2:

    def __init__(self):
        self.a = 1
        self.b = 100

    def __eq__(self, other):
        return self.a == other.a


ObK1 = K1()
ObK2 = K2()

print(ObK1)

print(ObK1 == ObK2)
