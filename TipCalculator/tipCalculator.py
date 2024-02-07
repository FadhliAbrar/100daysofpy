print("Welcome to the tip calculator")
totalBill = input("What was the total bill:\n")
personInCharge = input("How many people to split the bill?\n")
tipPersentage = input("What percentage tip would you like to give?(max 100% u're not rich)\n")

def func(bill, totalPerson, tipPercentage):
    eachPersonBill = (float(bill)*(float(tipPercentage)/100) + float(bill))/int(totalPerson)
    return float(eachPersonBill)

value = func(totalBill, personInCharge, tipPersentage)

print("Each person should pay: $", value)