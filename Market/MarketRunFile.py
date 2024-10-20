# Noah Taylor
# MarketApp

from marketmodel import MarketModel

def main():
    print("Welcome to the Noah Market Simulator!\n")
    lengthOfSimulation = int(input("Enter the total running time in minutes: "))
    averageTimePerCus = int(input("Enter the average processing time per customer in minutes: "))
    probabilityOfNewArrival = float(input("Enter the probability of a new customer (Enter 1): "))
    numCashiers = int(input("Enter the number of Cashiers in the Noah Market: "))
    
    if lengthOfSimulation < 1 or lengthOfSimulation > 1000:
        print("Running time must be an integer greater than 0 and less than or equal to 1000")
    elif averageTimePerCus <= 0 or averageTimePerCus >= lengthOfSimulation:
        print("Average time per customer must be an integer greater than 0 and less than running time")
    elif probabilityOfNewArrival <= 0 or probabilityOfNewArrival > 1:
        print("Probability must be inputted as 1")
    elif numCashiers < 1:
        print("Number of cashiers must be greater than 0")
    else:
        model = MarketModel(lengthOfSimulation, averageTimePerCus, probabilityOfNewArrival, numCashiers)
        model.runSimulation()
        print(model)

if __name__ == "__main__":
    main()

   
