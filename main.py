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

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("mashina km qaytarib bo'lmaydi.")


avto1 = Avto("Gm", "Malibu", "oq", "2015", 40000, 100000)
avto1.add_km(15000)
print(avto1.get_km())

# print(f"ID: {avto1.get_id()}")
# print(f"KM: {avto1.get_km()}")
