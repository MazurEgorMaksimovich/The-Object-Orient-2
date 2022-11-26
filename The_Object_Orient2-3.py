class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg
    
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы задаются только числами.')

    def to_pounds(self):
        return self.__kg * 2.205

kg_to_pound = KgToPounds(int(input("Введите массу предмета в кг: ")))
print("Это " + str(kg_to_pound.to_pounds()) + " фунтов.")