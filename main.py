from uuid import uuid4


class Avto:

    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id


avto1 = Avto("Gm", "Malibu", "oq", "2015", 40000, 10000)

print(f"ID: {avto1.get_id()}")
print(f"KM: {avto1.get_km()}")
