Kapital = int(input("What is the kapital?: "))
interestinpercentage = float(input("\nWhat is the interestrate in percentage?: "))
Years = int(input("\nHow many years is the interestrate being used: "))
sumafterinterest =float ("{0:.2f}".format( Kapital*pow((interestinpercentage/100)+1,Years)))
print("\nThe sum after", Years, "years is", sumafterinterest)
