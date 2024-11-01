# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)

from random import randint

class Train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, from_station, to_station):
        print(
            f"Ticket booked for train no: {self.train_no} from {from_station} to {to_station}"
        )

    def get_status(self):
        print(f"Train no: {self.train_no} is running on time")
        print(f"Number of seats available: {randint(0, 34)}")

    def get_fare(self, from_station, to_station):
        print(
            f"Ticket fare for train no: {self.train_no} form {from_station} to {to_station} is {randint(450,1060)}"
        )

booking = Train(78951)
booking.book_ticket("Karachi", "Multan")
booking.get_status()
booking.get_fare("Karachi", "Multan")
