from random import randint 


class Train:

    def __init__(self, trainNO):
        self.trainNO = trainNO
    def getStatus(self):
       print(f"Tranin no: {self.trainNO} is running on time") 

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNO} from {fro } to {to}") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no{self.trainNO} from {fro } to {to} is {randint(222, 5555)}") 


t = Train(12339)
t.book("Rampur", "Rajawatiya")
t.getStatus()
t.getFare("Rampur", "Birgunj")