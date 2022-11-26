class Soda:

    def __init__(self, dobav = ""):
        self.dobav = dobav
    
    def show_my_drink(self):
        if self.dobav == "":
            print("Обычная газировка.")
        else:
            print("Газировка и " + self.dobav + ".")


dobav = input("Выберите добавку к газировке: ")
soda = Soda(dobav)
soda.show_my_drink()