class animal:
    def speaks(self):
        print('animal speaks...')

class cow(animal):
    def meows(self):
        print("cow mows")

cow1 = cow()
cow1.speaks()
cow1.meows()