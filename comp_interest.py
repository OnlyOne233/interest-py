capital = int(input("how much money do you have saved? "))
time = int(input("for how many years do you intend to save? "))
rate = 1.02 #2% interest

def compound_interest(capital, rate, time):
    total_interest = rate**time
    sum = total_interest * capital
    return sum 

sum = compound_interest(capital, rate, time)
#print(sum)
print(f"With an interest rate of 2% you will have a total of {sum}$ saved after {time} years ")