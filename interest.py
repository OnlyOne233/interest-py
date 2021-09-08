principal = float(input("how much money do you have saved?"))
years = float(input("for how many years do you intend to save?"))
interest = int(input("how much is the interest rate?: "))
summa = ((1 + (interest / 100)) ** years) * principal
print(f"with an interest rate of {interest}% you will have a total of {summa}$ saved after {years} years ")
#testest
