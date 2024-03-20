# ====== CAPSTONE PROJECT 1 - VARIABLES AND CONTROL STRUCTURES ====== #

# *** NOTE *** # 
# This is a Python program allows the user to calculate either the amount of interest they'll earn 
# on their investment or the amount they'll have to pay on a home loan.
# The program will ask the user which one they want to calculate by inputing either
# 'INVESTMENT' to calculate interest earned or
# 'BOND' to calculate monthly repayment. 

# Selecting 'INVESTMENT' will then ask the user to input the following variables: amount of money deposited, interest rate, 
# number of years they plan to invest and whether they want to calculate simple or compound interest.
# The program will then calculate the amount of interest they'll earn using the formula:

# total interest earned = P (1 + r x t) - simple interest
# total interest earned = P (1 + r)^t - compound interest
# where  P = money deposited
#        r = interest rate / 100
#        t = number of years the money is invested for


# Selecting 'BOND' will ask the user to input the following: present value of the house, interest rate and 
# number of months they need to repay the bond.
# The program will then calculate the monthly bond repayment using the formula:

# monthly repayment = (i x P) / (1 - (1 + i)^-n)
# where  i = monthly interest rate
#        n = number of months the bond will be repaid

# The calculated values will be outputed as a print statement displaying either total interest or monthly bond repayment 
# rounded to two decimal places.

# *** NOTE END *** #


import math

# Displaying the definition for each calculation the user wants to do
intro = '''
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
'''
print (intro)

chosen_calculation = input ("Enter either 'investment' or 'bond' from the menu above to proceed:").upper() #capitalising input to allow multiple capitalisation styles  
                                                                                                                      


# === BRANCH FOR INVESTMENT OPTION === #
if chosen_calculation == "INVESTMENT":
    
   # Collecting all required user inputs and casting numerical inputs into floats
    money_in = float (input ("Thank you. Please input the amount of money you are investing:"))
    interest_rate = float (input ("Please input the interest rate (without %):"))
    invest_year = float (input ("How many years do you plan on investing?"))
    interest = input ("Would you like to calculate simple or compound interest?").upper()

    # Branch for simple interest #
    if interest == "SIMPLE":
        
        total_interest = money_in * (1 + (interest_rate/100) * invest_year)
        print ("The amount of interest you'll earn on your investment is {:0.2f} ".format (total_interest))

    # Branch for compound interest #
    elif interest == "COMPOUND":
        
        total_interest = money_in * math.pow (1 + (interest_rate/100), invest_year)
        print ("The amount of interest you'll earn on your investment is {:0.2f} ".format (total_interest))

    # Error message for invalid inputs #
    else:
        print("Please input either 'simple' or 'compound'.") 


# === BRANCH FOR BOND OPTION === #
elif chosen_calculation == "BOND":
    
    # Collecting all required user inputs and casting numerical inputs into floats
    house_val = float (input ("Thank you. Please input the present value of the house:"))
    interest_rate = float (input ("Please input the interest rate:"))
    repay_time = float (input ("How many months do you require to repay the bond?"))
    monthly_int_rate = (interest_rate/100)/12 #Calculating monthly interest rate

    repayment = (monthly_int_rate * house_val) / (1 - (1 + monthly_int_rate) ** (repay_time * -1))
    print ("You will have to repay {:0.2f} per month for your home loan".format (repayment))


# Error message for invalid inputs #
else:
    print ("Please input either 'investment' or 'bond'.") 
