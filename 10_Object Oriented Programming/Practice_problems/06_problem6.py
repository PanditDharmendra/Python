from random import randint 


class Train:

    def __init__(slf, trainNO):
        slf.trainNO = trainNO
    def getStatus(harry):
       print(f"Tranin no: {harry.trainNO} is running on time") 

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNO} from {fro } to {to}") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no{self.trainNO} from {fro } to {to} is {randint(222, 5555)}") 


t = Train(12339)
t.book("Rampur", "Rajawatiya")
t.getStatus()
t.getFare("Rampur", "Birgunj")