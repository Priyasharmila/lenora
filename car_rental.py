import datetime 
class CarRental:
    def __init__(self, stock=0):
        self.stock = stock
    def displayStock(self):
        print("Currently {} cars are available to rent.".format(self.stock))
        return self. stock
    def rentCarOnHourlyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! Currently {} cars are available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n, now.hour))
            self.stock -= n 
            return now
    def rentCarOnDailyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! Currently {} cars are available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on daily basis today at {} hours.".format(n, now.hour))
            self.stock -= n
            return now
    def rentCarOnWeeklyBasis(self, n):
        if n <= 0: 
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! Currently {} cars are available to rent.".format(self.stock)) 
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on weekly basis today at {} hours.".format(n, now.hour))
            self.stock -= n
            return now
    def returnCar(self, request):
        rentalTime, rentalBasis, numOfCars = request 
        bill = 0
        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars 
            now = datetime.datetime.now() 
            rentalPeriod = now - rentalTime
        if rentalBasis == 1: # hourly 
            bill = round(rentalPeriod.seconds / 3600) * 5 * numOfCars 
        elif rentalBasis == 2: # daily 
            bill = round(rentalPeriod.days) * 120 * numOfCars 
        elif rentalBasis == 3: # weekly 
            bill = round(rentalPeriod.days / 7) * 360 * numOfCars 
            if (2 <= numOfCars): 
                print("You have a 20% discount!") 
                bill = bill * 0.8 
                return bill


class Customer: 
    def __init__(self): 
        self.cars = 0 
        self.rentalBasis = 0 
        self.rentalTime = 0 
        self.bill = 0 
    def requestCar(self): 
        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError: 
            print("That's not a positive integer!")
            return -1 
        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
            return self.cars 
    def returnCar(self):
        if self.rentalBasis and self.rentalTime and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars
        else:
            return 0, 0, 0

