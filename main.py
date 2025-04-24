print("@@@@ SCSU Jobs Portal @@@@")
print("1. View Jobs")
print("2. Login")
print("0. Exit")


while True:
    try:
        choice = int(input("Enter option: "))
        if choice < 0 or choice > 2:
            print("Please enter either 0, 1 or 2.")
        else:
            break
    except:
        print("Please enter a valid number.")