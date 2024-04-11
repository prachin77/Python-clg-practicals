class Housekeeper:
    def __init__(self):
        self.plants = ['Plant1', 'Plant2', 'Plant3', 'Plant4', 'Plant5', 'Plant6', 'Plant7', 'Plant8']

    def display_plants(self):
        print("Plants arrangement:", self.plants)

    def arrange_equally(self):
        mid = len(self.plants) // 2
        left_side = self.plants[:mid]
        right_side = self.plants[mid:]
        self.plants = left_side + right_side

    def replace_destroyed(self, destroyed_plants, new_plant_type):
        for i in range(len(self.plants)):
            if self.plants[i] in destroyed_plants:
                self.plants[i] = new_plant_type

    def rearrange(self):
        self.plants = self.plants[4:] + self.plants[:4]



housekeeper = Housekeeper()


print("Initial arrangement:")
housekeeper.display_plants()


housekeeper.arrange_equally()
print("\nArranged equally on both sides:")
housekeeper.display_plants()


destroyed_plants = ['Plant3', 'Plant5']
new_plant_type = 'Plant9'  
housekeeper.replace_destroyed(destroyed_plants, new_plant_type)
print("\nReplaced destroyed plants:")
housekeeper.display_plants()


housekeeper.rearrange()
print("\nRearranged plants:")
housekeeper.display_plants()
