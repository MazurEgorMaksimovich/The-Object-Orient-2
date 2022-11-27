class Human:
    default_name = 'Кузьма'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._house = None
    
    def info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Money: " + str(self._money))
        print("House: " + str(self._house))
    
    @staticmethod
    def default_info():
        print("Default Name: " + Human.default_name)
        print("Default Age: " + str(Human.default_age))
    
    def __make_deal(self, house, house_price):
        self._money -= house_price
        self._house = house
    
    def earn_money(self, money):
        self._money += money
        print("Earned " + str(money) + " money! Current value: " + str(self._money) + ".")
    
    def buy_house(self, house, discount):
        house_price = house.final_price(discount)
        print("Final Price: " + str(house.final_price(discount)))
        if float(self._money) < house_price:
            print("Not enough money!")
        else:
            self.__make_deal(house, house_price)

class House:

    def __init__(self, price, area):
        self.price = price
        self.area = area
    
    def final_price(self, discount):
        return self.price - self.price*(discount/100)

class SmallStandartHouse(House):
    def __init__(self, price):
        self.area = 40
        super().__init__(price, self.area)

Human.default_info()
human = Human("Клим", 21)
human.info()
smallstandarthouse = SmallStandartHouse(20000)
human.buy_house(smallstandarthouse, 20)
human.earn_money(5000)
human.earn_money(20000)
human.buy_house(smallstandarthouse, 20)
human.info()