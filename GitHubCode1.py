class Ticket:
    def __init__(self, staff_id, name, email, problem, password, genpass):
        self.staff = staff_id
        self.name = name
        self.email = email
        self.problem = problem
        self.password = password
        self.genpass = genpass


def submit():
    print("Please Answer the following questions so we can help resolve your ticket as quickly as possible!")

    get_staff_id = input("ID: ")
    get_name = input("name: ")
    get_email = input("email: ")
    get_problem = input("Please state the problem you are having:")
    get_password = get_staff_id[0:2] + get_name[0:3]
    get_gen_pass = input("new password Y/N?: ")
    ticket = Ticket(get_staff_id, get_name, get_email, get_problem, get_password, get_gen_pass)
    if get_gen_pass == "Y":
        print("Here is your new password: " + get_password)
        input("Press ENTER to return to the home-screen")
    else:
        print("\nThank you...ticket has been submitted successfully!")
        input("Press ENTER to return to the home-screen")

    return ticket

#One part I found intersting was trying to get the ticket to display in the def show() function.
#I didn't fully grasp how to display the ticket stats here as it would always end up printing an empty ticket ([])

def show(ticket):
    print(ticket)
    input("Press ENTER to return to home-screen")


#The loop I used for the menu was an interesting part of code I found challenging.

#It took me a long time to figure out how to get the loop to work successfully, without conflicting with other functions.


def menu():
    print("Welcome. Please select option:")
    print()
    tickets = []
    choice = input("""
0: Exit
1: Submit
2: Show tickets
3: Respond to ticket
4: Re-open tickets
5: Display ticket stats
choice: """)
    if choice == "0":
        return 0
    elif choice == "1":
        (tickets.append(submit()))
    elif choice == "2":
        show(tickets)
    elif choice == "3":
        respond()
    elif choice == "4":
        reopen()
    elif choice == "5":
        display()
    else:
        print("You must only select either 0-5")
        print("Please try again")
    return 1


def main():
    while menu():
        continue


def respond():
    input("Please provide ticket number you wish to respond to: ")


def reopen():
    input("Please provide ticket number you wish to re-open: ")


def display():
    print("Ticket Statistics: ")
    print()
    input("Press ENTER to return to menu")


main()
