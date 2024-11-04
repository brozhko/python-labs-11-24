class Ship:
    def __init__(self, tonnage=0, name="", seats_number=0):

        self.__tonnage = tonnage
        self.__name = name
        self.__seats_number = seats_number
        self.num = 1
        self.line = ""

    def get_tonnage(self):
        return self.__tonnage

    def get_name(self):
        return self.__name

    def get_seats_number(self):
        return self.__seats_number

    def __str__(self):
        return f"Ship: {self.__tonnage}"

    def __repr__(self):
        return f"Ship: {self.__tonnage}, {self.__name}, {self.__seats_number}"

    def __del__(self):
        print("Видалено")

if __name__ == "__main__":
    Ship1 = Ship(100, "Titanik", 1120)
    Ship2 = Ship(200, "Rivera", 1234)
    Ship3 = Ship(300, "Atalanta", 1232)
    print(Ship1.get_name())
    print(Ship1.get_tonnage())
    print(Ship1.get_seats_number())
