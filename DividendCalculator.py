goal = 20400

monthlyInvest = 1000
yearlyYield = 0.03
currentInvest = 5000
currentDividend = 0
yearlyGrowth = 0.0025

month = 0
while currentDividend * 4 < goal:
    month += 1
    currentInvest += monthlyInvest
    if month % 3 == 0:
        currentDividend = (currentInvest * (yearlyYield/4)) * 0.85
        currentInvest = currentInvest + currentDividend
    if month % 12 == 0:
        currentInvest = currentInvest * (1 + yearlyGrowth)

     
print(f'${currentInvest:,.2f}')
print(f'${currentDividend:,.2f}')
print(str(month/12) + ' years')