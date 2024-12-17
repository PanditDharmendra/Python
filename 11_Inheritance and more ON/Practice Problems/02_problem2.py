class Animals:
    @staticmethod
    def animal():
        print("Hi I am animal")


class pets(Animals):
    @staticmethod
    def pet():
        print("Pet is good")

class dog(pets):
    @staticmethod
    def Brak():
        print("Bow Bow!")

d = dog()
d.Brak()
d.pet()
d.animal()