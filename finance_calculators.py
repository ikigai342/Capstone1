<<<<<<< HEAD
# Program has two financial calculators where the user can calculate:
# The amount of simple or compound interest they will receive over a given time
# The amount of money needs to be repaid on their bond over a given time


print("""
Choose either 'investment or ''bond' from the menu below to proceed:

investment \t- to calculate the amount of interest you'll earn on interest
bond \t\t- to calculate the amount you'll have to pay on a home loan
""")
calc_type = input("(i) investment / (b) bond: ")
calc_type = calc_type.lower()

# Calculates and prints the total interest amount gathered
if (calc_type == 'i') or (calc_type == "investment"):
    deposit_amount = float(input("Enter the amount of money you"
                                + "want to deposit: "))
    interest_rate = float(input("Enter the amount of interest % you"
                                + "want to accumulate: "))   
    interest_length = int(input("Enter the amount of years you plan "
                                + "on investing: "))

    # Takes user interest value and change the interest percentage
    interest_rate /= 100

    interest = input("Do you want (s) simple or (c) compound: ")
    interest = interest.lower()

    if (interest == "simple") or (interest == "s"):
        # Simple Interest = P*(1 + r * t)
        interest_amount = 1 + interest_rate * interest_length
        interest_amount = deposit_amount * interest_amount
    elif (interest == "compound") or (interest == "c"):
        # Compound Interest = P*(1 + r) ^ t
        interest_amount = (1 + interest_rate) ** interest_length
        interest_amount = deposit_amount * interest_amount
    else:
        print("\ninvalid interest type please enter a valid input.")

    interest_amount = round(interest_amount,2)

    print(f"\nYou're total interest is R{interest_amount}")

# Calculates and prints the monthly bond payment
elif (calc_type == 'b') or (calc_type == "bond"):
    house_value = float(input("Enter the value of the house: "))
    bond_interest = float(input("Enter the amount of interest on the bond: "))
    bond_length = int(input("Enter the amount of months you want" 
                            +"to pay the bond back: "))

    # Takes user interest value and change the interest to a monthly percentage
    bond_interest /= 100
    bond_interest /= 12

    # Calculates the monthly bond payments needed to needed to pay back and 
    # prints it for the user Bond Payment = (i * P)/(1 - (1 + i) ^ -n)
    payment = bond_interest * house_value
    payment = payment/(1 - (1+bond_interest) ** (-bond_length))
    payment = round(payment,2)

    print(f"\nYou're monthly payments will be R{payment}")

# Prints out error if no valid calculation type is selected
else:
    print("\nInvalid input please enter a valid input.")
=======
# Program has two financial calculators where the user can calculate:
# The amount of simple or compound interest they will receive over a given time
# The amount of money needs to be repaid on their bond over a given time


print("""
Choose either 'investment or ''bond' from the menu below to proceed:

investment \t- to calculate the amount of interest you'll earn on interest
bond \t\t- to calculate the amount you'll have to pay on a home loan
""")
calc_type = input("(i) investment / (b) bond: ")
calc_type = calc_type.lower()

# Calculates and prints the total interest amount gathered
if (calc_type == 'i') or (calc_type == "investment"):
    deposit_amount = float(input("Enter the amount of money you"
                                + "want to deposit: "))
    interest_rate = float(input("Enter the amount of interest % you"
                                + "want to accumulate: "))   
    interest_length = int(input("Enter the amount of years you plan "
                                + "on investing: "))

    # Takes user interest value and change the interest percentage
    interest_rate /= 100

    interest = input("Do you want (s) simple or (c) compound: ")
    interest = interest.lower()

    if (interest == "simple") or (interest == "s"):
        # Simple Interest = P*(1 + r * t)
        interest_amount = 1 + interest_rate * interest_length
        interest_amount = deposit_amount * interest_amount
    elif (interest == "compound") or (interest == "c"):
        # Compound Interest = P*(1 + r) ^ t
        interest_amount = (1 + interest_rate) ** interest_length
        interest_amount = deposit_amount * interest_amount
    else:
        print("\ninvalid interest type please enter a valid input.")

    interest_amount = round(interest_amount,2)

    print(f"\nYou're total interest is R{interest_amount}")

# Calculates and prints the monthly bond payment
elif (calc_type == 'b') or (calc_type == "bond"):
    house_value = float(input("Enter the value of the house: "))
    bond_interest = float(input("Enter the amount of interest on the bond: "))
    bond_length = int(input("Enter the amount of months you want" 
                            +"to pay the bond back: "))

    # Takes user interest value and change the interest to a monthly percentage
    bond_interest /= 100
    bond_interest /= 12

    # Calculates the monthly bond payments needed to needed to pay back and 
    # prints it for the user Bond Payment = (i * P)/(1 - (1 + i) ^ -n)
    payment = bond_interest * house_value
    payment = payment/(1 - (1+bond_interest) ** (-bond_length))
    payment = round(payment,2)

    print(f"\nYou're monthly payments will be R{payment}")

# Prints out error if no valid calculation type is selected
else:
    print("\nInvalid input please enter a valid input.")
>>>>>>> refs/remotes/cap1/master
