
# Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information of train running under Indian Railway
from random import randint

class Train:
    def __init__(self, trainNo, totalSeats):
        self.trainNo = trainNo
        self.totalSeats = totalSeats
        self.bookedSeats = 0

    def book(self, fro, to):
        if self.bookedSeats < self.totalSeats:
            self.bookedSeats += 1
            print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        else:
            print("No seats available")

    def getStatus(self):
        availableSeats = self.totalSeats - self.bookedSeats
        print(f"Train no: {self.trainNo} has {availableSeats} seats available")

    def getFare(self, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {fare}")

# Example usage
t = Train(1226, 100)
t.book("Kolkata", "Mumbai")
t.getStatus()
t.getFare("Kolkata", "Mumbai")
