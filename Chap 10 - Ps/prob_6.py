# 6. Can you change the self-parameter inside a class to something else (say “harry”).
# Try changing self to “slf” or “harry” and see the effects.

from random import randint


class Train:

    def __init__(
        slf, train_no
    ):  # changed self to slf and nothing happened the result is same
        slf.train_no = train_no

    def book_ticket(self, from_station, to_station):
        print(
            f"Ticket booked for train no: {self.train_no} from {from_station} to {to_station}"
        )

    def get_status(
        harry,
    ):  # changed self to harry  and nothing happened the result is same
        print(f"Train no: {harry.train_no} is running on time")
        print(f"Number of seats available: {randint(0, 34)}")

    def get_fare(self, from_station, to_station):
        print(
            f"Ticket fare for train no: {self.train_no} form {from_station} to {to_station} is {randint(450,1060)}"
        )


booking = Train(78951)
booking.book_ticket("Karachi", "Multan")
booking.get_status()
booking.get_fare("Karachi", "Multan")
