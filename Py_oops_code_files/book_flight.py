# Exercise 28: Flight Class with Passenger Capacity Check

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight():

    def __init__(self, flight_code, seat_capacity):
        self.flight_code = flight_code
        self.seat_capacity = seat_capacity
        self.booked_passengers = []

    def book_flight(self, Passenger):
        if len(self.booked_passengers) < self.seat_capacity:
            self.booked_passengers.append('Passenger.name')
            print(f'{Passenger.name} is booked on Flight {self.flight_code} sucessfully.')
        else:
            print(f'Sorry, Flight {self.flight_code} is fully booked.')


flight1 = Flight('AI101', 2)
flight1.book_flight(Passenger('Kalam'))
flight1.book_flight(Passenger('Tiru'))
flight1.book_flight(Passenger('Renu'))