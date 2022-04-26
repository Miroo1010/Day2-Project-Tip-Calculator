#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Intro
title="Welcome to the tip calculator!".center(63,"-")
print(title + "\n" + "\n")

# Inputs
total_bill=float(input("what was the total bill? $"))

tip=int(input("what percentage tip would you like to give? 10, 12, or 15% ? "))

client_qte=int(input("How many people to split the bill? "))

# Calculator

bill_charged=total_bill * (1+tip/100)

indiv_pay="{:.2f}".format(bill_charged / client_qte )

print(f" \n --> Each person should pay ${indiv_pay} \n ")
print("Thank you!".center(60,"*"))



