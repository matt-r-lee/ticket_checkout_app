TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


# Function created to calculate customer's ticket price
def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Runs as long as there are still tickets available
while tickets_remaining > 0:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("Please provide your name.  ")
    num_tickets = input("Hi {}! How many tickets would you like to purchase?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("We are having a problem processing your request. {} Please try again.".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Okay, got it. The total amount for your ticket(s) is ${} (There is a service charge of ${}.).".format(amount_due,SERVICE_CHARGE))
        confirm = input("Would you like to continue? Y/N?  ")
        if confirm.lower() == "y":
            print("Thank you for your purchase!")
            tickets_remaining -= num_tickets
        elif confirm.lower() == "n":
            print("Okay, if you woud change your mind {} feel free to come back!".format(name))
        else:
            print("I'm sorry, that is not a valid response. Please try again later.  ")

# Once tickets are sold out, alerts system/user
print("Sorry the tickets are all sold out.")
