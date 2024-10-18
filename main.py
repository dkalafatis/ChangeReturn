def calculate_change(cost, given):
    # Calculate total change
    change = given - cost

    # Convert change to cents for easier calculation
    change_in_cents = round(change * 100)

    # Calculate the number of quarters
    quarters = change_in_cents // 25
    change_in_cents %= 25

    # Calculate the number of dimes
    dimes = change_in_cents // 10
    change_in_cents %= 10

    # Calculate the number of nickels
    nickels = change_in_cents // 5
    change_in_cents %= 5

    # The remaining change_in_cents are pennies
    pennies = change_in_cents

    return quarters, dimes, nickels, pennies


# Input from the user
cost = float(input("Enter the total cost of the item: "))
given = float(input("Enter the amount of money given: "))

# Ensure the given amount is not less than the cost
if given < cost:
    print("The given amount cannot be less than the cost of the item.")
else:
    # Calculate and display the change
    quarters, dimes, nickels, pennies = calculate_change(cost, given)
    print(f"Change owed: {given - cost:.2f}")
    print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}")
