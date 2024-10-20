# Noah Taylor
# Market run app

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):
    def __init__(self, lengthOfSimulation, averageTimePerCus,probabilityOfNewArrival, numCashiers):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.cashier = [Cashier(i) for i in range(numCashiers)]

   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self.probabilityOfNewArrival,
                currentTime,
                self.averageTimePerCus)

            # Send customer to cashier if successfully generated
            if customer != None:
                cashier = random.choice(self.cashier)
                cashier.addCustomer(customer)

            # Tell cashier to provide another unit of service
            for cashier in self.cashier:
                cashier.serveCustomers(currentTime)

    def __str__(self):
        #display results for cashier at end of the program
        results = ""
        for cashier in self.cashier:
            results += f"Results for Cashier {cashier.cashierNumber}:\n{cashier}\n"
        return results
