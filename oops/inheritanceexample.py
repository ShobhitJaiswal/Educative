class Animal:
    # properties
    multicellular = True
    # Eukaryotic means Cells with Nucleus
    eukaryotic = True
    
    # functions
    def breath(self):return True

    def feed(self):pass

class Mammal(Animal):
	# properties
	haveMammaryGland = True
	warmBlood = True
	
	# functions
	def produceMilk(self):pass

class Amphibian(Animal):
	# properties
	liveInWater = True
	
	# functions
	def metamorphosis(self):return True

frog = Amphibian()
print(frog.breath())
print(frog.metamorphosis())
print(frog.liveInWater)