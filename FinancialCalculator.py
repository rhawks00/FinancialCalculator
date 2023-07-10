import os

def calculate():
    
    toReturn = int(input("Initial amount: "))
    savings = int(input("Monthly added: "))
    months = int(input("Months of compound: "))
    interestRate = float(input("Interest rate: "))
    goal = int(input("Enter your goal amount: "))
    
    interestPercent = (((interestRate / 100)/12) + 1)
    monthsToGoal = "more"
    metGoal = True
    
    for i in range(0, months):
        toReturn+=savings
        toReturn*=interestPercent
        if toReturn > goal and metGoal:
            monthsToGoal = i + 1
            metGoal = False
    
    print("You will have $" + str(round(toReturn,2)) + " after " + str(months) + " months of saving with an interest rate of %" + str(interestRate) + ".")
    print("It will take " + str(monthsToGoal) + " months to reach your goal.")
    print("")

def main():
 os.system('cls')
 while True:
    calculate()
    toContinue = input("Would you like to do another calculation? y or n ")
    if toContinue == "n":
        os.system('cls')
        quit()
    print("")
    
if __name__ == "__main__":
   main()
 