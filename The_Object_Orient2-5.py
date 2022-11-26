class Tomato:
    states = ["missing", "flower", "green_tomato", "red_tomato"]

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]
    
    def grow(self):
        self._state = Tomato.states[Tomato.states.index(self._state) + 1]
    
    def is_ripe(self):
        if Tomato.states.index(self._state) == 3:
            return True
        else:
            return False

class TomatoBush:

    def __init__(self, tomato_kol):
        self.tomato_kol = tomato_kol
        self.tomatoes = []
        for _ in range(self.tomato_kol):
            tomato = Tomato(_)
            self.tomatoes.append(tomato)
    
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato._state = Tomato.states[Tomato.states.index(tomato._state) + 1]
            print("Tomato " + str(tomato._index) + " is " + tomato._state)
    
    def all_are_ripe(self):
        riped_tomatoes = 0
        for tomato in self.tomatoes:
            if Tomato.states.index(tomato._state) == 3:
                riped_tomatoes += 1
        if riped_tomatoes == len(self.tomatoes):
            return True
        else:
            print("Too early! Your plant is green and not ripe.")
            return False
    
    def give_away_all(self):
        self.tomatoes = []
        print("Gardener is harvesting...")
        print("Harvesting is finished.")

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    
    def work(self):
        print("Gardener is working...")
        self._plant.grow_all()
        print("Gardener finished.")
    
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
    
    @staticmethod
    def knowledge_base():
        print \
            ("""
Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.
            """)



Gardener.knowledge_base()
tomatobush = TomatoBush(3)
gardener = Gardener("Васятка", tomatobush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()