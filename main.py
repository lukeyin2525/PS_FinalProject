#Function to check input, takes 3 parameters -  question to ask, lower limit of the input, upper limit of the inputs
def check_input(question, lower, upper):
    while True:
        try:
            choice = int(input(question))
            if choice < lower or choice > upper:
                print("Please enter either 0, 1 or 2.")
            else:
                return choice
        except:
            print("Please enter a valid number.")

#Start of main code

print("@@@@ SCSU Jobs Portal @@@@")
print("1. View Jobs")
print("2. Login")
print("0. Exit")

check_input("Enter option: ", 0, 2)

def company():

    print(" 1) Edit Company Profile")
    print(" 2) View jobs posted")
    print(" 3) Add new job")

    option = check_input("Enter option: ", 1, 3)